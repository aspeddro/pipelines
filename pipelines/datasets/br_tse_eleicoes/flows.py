# -*- coding: utf-8 -*-
"""
Flows for br_tse_eleicoes
"""
# pylint: disable=invalid-name,line-too-long
from datetime import timedelta

from prefect import Parameter, case
from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefect.tasks.prefect import create_flow_run, wait_for_flow_run

from pipelines.constants import constants
from pipelines.datasets.br_tse_eleicoes.constants import constants as tse_constants
from pipelines.datasets.br_tse_eleicoes.tasks import (
    download_urls,
    preparing_data,
    get_data_source_max_date,
    preparing_data_bens_candidato

)
from pipelines.utils.constants import constants as utils_constants
from pipelines.utils.decorators import Flow
from pipelines.utils.execute_dbt_model.constants import constants as dump_db_constants
from pipelines.utils.tasks import (
    create_table_and_upload_to_gcs,
    get_current_flow_labels,
    rename_current_flow_run_dataset_table,
    # update_metadata,
)

from pipelines.utils.metadata.tasks import (
    check_if_data_is_outdated,
    update_django_metadata,
)

with Flow(
    name="br_tse_eleicoes.candidatos", code_owners=["lucas_cr"]
) as br_tse_candidatos:

    # Parameters

    dataset_id = Parameter("dataset_id", default="br_tse_eleicoes", required=True)

    table_id = Parameter("table_id", default="candidatos", required=True)

    materialization_mode = Parameter(
        "materialization_mode", default="dev", required=False
    )

    materialize_after_dump = Parameter(
        "materialize_after_dump", default=False, required=False
    )
    dbt_alias = Parameter("dbt_alias", default=False, required=False)

    update_metadata = Parameter("update_metadata", default=False, required=False)

    rename_flow_run = rename_current_flow_run_dataset_table(
        prefix="Dump: ", dataset_id=dataset_id, table_id=table_id, wait=table_id
    )

    data_source_max_date = get_data_source_max_date(upstream_tasks=[rename_flow_run])

    outdated = check_if_data_is_outdated(
        dataset_id=dataset_id,
        table_id=table_id,
        data_source_max_date=data_source_max_date,
        date_format="%Y-%m-%d",
        upstream_tasks=[data_source_max_date],
    )

    with case(outdated, True):

        gfiles_task = download_urls(urls=tse_constants.CANDIDATOS_URLS.value,
                                    upstream_tasks=[outdated])

        data = preparing_data(upstream_tasks=[gfiles_task])

        wait_upload_table = create_table_and_upload_to_gcs(
        data_path="/tmp/data/output",
        dataset_id=dataset_id,
        table_id=table_id,
        dump_mode="append",
        upstream_tasks=[data]
        )

      # materialize municipio_exportacao
        with case(materialize_after_dump, True):
            # Trigger DBT flow run
            current_flow_labels = get_current_flow_labels()
            materialization_flow = create_flow_run(
                flow_name=utils_constants.FLOW_EXECUTE_DBT_MODEL_NAME.value,
                project_name=constants.PREFECT_DEFAULT_PROJECT.value,
                parameters={
                    "dataset_id": dataset_id,
                    "table_id": table_id,
                    "mode": materialization_mode,
                    "dbt_alias": dbt_alias,
                    "dbt_command": "run/test",
                    "disable_elementary": False,
                    "download_csv_file": False
                },
                labels=current_flow_labels,
                run_name=f"Materialize {dataset_id}.{table_id}",
                upstream_tasks=[wait_upload_table]
            )

            wait_for_materialization = wait_for_flow_run(
                materialization_flow,
                stream_states=True,
                stream_logs=True,
                raise_final_state=True,

            )
            wait_for_materialization.max_retries = (
                dump_db_constants.WAIT_FOR_MATERIALIZATION_RETRY_ATTEMPTS.value
            )
            wait_for_materialization.retry_delay = timedelta(
                seconds=dump_db_constants.WAIT_FOR_MATERIALIZATION_RETRY_INTERVAL.value
            )
            # coverage updater

        with case(update_metadata, True):
            update_django_metadata(
                dataset_id=dataset_id,
                table_id=table_id,
                historical_database=False,
                date_format="%Y-%m-%d",
                prefect_mode=materialization_mode,
                bq_project="basedosdados",
                upstream_tasks=[wait_for_materialization],
            )

br_tse_candidatos.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
br_tse_candidatos.run_config = KubernetesRun(image=constants.DOCKER_IMAGE.value)
br_tse_candidatos.schedule = None



with Flow(
    name="br_tse_eleicoes.bens_candidato", code_owners=["lucas_cr"]
) as br_tse_bens_candidato:

    # Parameters

    dataset_id = Parameter("dataset_id", default="br_tse_eleicoes", required=True)

    table_id = Parameter("table_id", default="bens_candidato", required=True)

    materialization_mode = Parameter(
        "materialization_mode", default="dev", required=False
    )

    materialize_after_dump = Parameter(
        "materialize_after_dump", default=False, required=False
    )
    dbt_alias = Parameter("dbt_alias", default=False, required=False)

    update_metadata = Parameter("update_metadata", default=False, required=False)

    rename_flow_run = rename_current_flow_run_dataset_table(
        prefix="Dump: ", dataset_id=dataset_id, table_id=table_id, wait=table_id
    )

    data_source_max_date = get_data_source_max_date()

    outdated = check_if_data_is_outdated(
        dataset_id=dataset_id,
        table_id=table_id,
        data_source_max_date=data_source_max_date,
        date_format="%Y-%m-%d",
        upstream_tasks=[data_source_max_date],
    )

    with case(outdated, True):

        gfiles_task = download_urls(urls=[tse_constants.BENS_CANDIDATOS24.value],
                                    upstream_tasks=[outdated])

        data = preparing_data_bens_candidato(upstream_tasks=[gfiles_task])

        wait_upload_table = create_table_and_upload_to_gcs(
        data_path="/tmp/data/output",
        dataset_id=dataset_id,
        table_id=table_id,
        dump_mode="append",
        upstream_tasks=[data]
        )

      # materialize municipio_exportacao
        with case(materialize_after_dump, True):
            # Trigger DBT flow run
            current_flow_labels = get_current_flow_labels()
            materialization_flow = create_flow_run(
                flow_name=utils_constants.FLOW_EXECUTE_DBT_MODEL_NAME.value,
                project_name=constants.PREFECT_DEFAULT_PROJECT.value,
                parameters={
                    "dataset_id": dataset_id,
                    "table_id": table_id,
                    "mode": materialization_mode,
                    "dbt_alias": dbt_alias,
                    "dbt_command": "run/test",
                    "disable_elementary": False,
                },
                labels=current_flow_labels,
                run_name=f"Materialize {dataset_id}.{table_id}",
                upstream_tasks=[wait_upload_table],
            )

            wait_for_materialization = wait_for_flow_run(
                materialization_flow,
                stream_states=True,
                stream_logs=True,
                raise_final_state=True,
            )
            wait_for_materialization.max_retries = (
                dump_db_constants.WAIT_FOR_MATERIALIZATION_RETRY_ATTEMPTS.value
            )
            wait_for_materialization.retry_delay = timedelta(
                seconds=dump_db_constants.WAIT_FOR_MATERIALIZATION_RETRY_INTERVAL.value
            )
            # coverage updater

        with case(update_metadata, True):
            update_django_metadata(
                dataset_id=dataset_id,
                table_id=table_id,
                historical_database=False,
                date_format="%Y-%m-%d",
                prefect_mode=materialization_mode,
                bq_project="basedosdados-dev",
                upstream_tasks=[wait_for_materialization],
            )

br_tse_bens_candidato.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
br_tse_bens_candidato.run_config = KubernetesRun(image=constants.DOCKER_IMAGE.value)
br_tse_bens_candidato.schedule = None