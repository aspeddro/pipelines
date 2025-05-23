# -*- coding: utf-8 -*-
"""
Flows for temporal_coverage_updater
"""

from prefect import Parameter
from prefect.run_configs import KubernetesRun
from prefect.storage import GCS

from pipelines.constants import constants
from pipelines.utils.decorators import Flow
from pipelines.utils.metadata.tasks import (
    create_update_quality_checks,
    query_tests_results,
    update_django_metadata,
)

with Flow(
    name="update_temporal_coverage_teste",
    code_owners=[
        "lauris",
    ],
) as temporal_coverage_updater_flow:
    dataset_id = Parameter("dataset_id", required=True)
    table_id = Parameter("table_id", required=True)
    target = Parameter("target", default="prod", required=False)
    coverage_type = Parameter(
        "coverage_type", default="part_bdpro", required=False
    )
    date_column_name = Parameter(
        "date_column_name",
        default={"month": "mes", "year": "ano"},
        required=False,
    )
    date_format = Parameter("date_format", default="%Y-%m", required=False)
    time_delta = Parameter("time_delta", default={"months": 6}, required=False)

    update_django_metadata(
        dataset_id=dataset_id,
        table_id=table_id,
        date_column_name=date_column_name,
        date_format=date_format,
        coverage_type=coverage_type,
        time_delta=time_delta,
        prefect_mode=target,
        bq_project="basedosdados",
    )

temporal_coverage_updater_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
temporal_coverage_updater_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value
)
# flow.schedule = every_two_weeks


with Flow(
    name="create_update_quality_checks",
    code_owners=[
        "equipe_pipelines",
    ],
) as quality_checks_updater:
    tests_results = query_tests_results()
    results = create_update_quality_checks(
        tests_results=tests_results, upstream_tasks=[tests_results]
    )


quality_checks_updater.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
quality_checks_updater.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value
)
# quality_checks_updater.schedule = every_day_quality_checks
