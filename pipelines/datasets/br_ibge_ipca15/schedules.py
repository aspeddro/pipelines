"""
Schedules for br_ibge_ipca15
"""

from datetime import timedelta, datetime
from prefect.schedules import Schedule
from prefect.schedules.clocks import IntervalClock
from pipelines.constants import constants

every_month = Schedule(
    clocks=[
        IntervalClock(
            interval=timedelta(days=30),
            start_date=datetime(2021, 1, 1),
            labels=[
                constants.BASEDOSDADOS_PROD_AGENT_LABEL.value,
            ]
        )
    ]
)