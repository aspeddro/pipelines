# -*- coding: utf-8 -*-
"""
Schedules for br_rf_cno
"""


# -*- coding: utf-8 -*-
"""
Schedules for br_rf_cafir
"""

from datetime import datetime

from prefect.schedules import Schedule, adjustments, filters
from prefect.schedules.clocks import CronClock

from pipelines.constants import constants

schedule_br_rf_cno = Schedule(
    clocks=[
        CronClock(
            #trocar cron clock
            cron="0 0 * * *",
            start_date=datetime(2023, 9, 1, 0, 0),
            labels=[
                constants.BASEDOSDADOS_PROD_AGENT_LABEL.value,
            ],
            parameter_defaults={
                "dataset_id": "br_rf_cno",
                "table_id": "microdados",
                "materialization_mode": "prod",
                "materialize_after_dump": True,
                "update_metadata": True,
                "dbt_alias": True,
            },
        )
    ],
    filters=[filters.is_weekday],
    adjustments=[adjustments.next_weekday],
)
