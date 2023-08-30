from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from . import assets

all_assets = load_assets_from_modules([assets])

# Define a job that will materialize the assets
dagster_crawler_agendamento_job = define_asset_job("dagster_crawler_agendamento_job", selection=AssetSelection.all())

# Define a ScheduleDefinition for the job it should run and a cron schedule of how frequently to run it
dagster_crawler_agendamento = ScheduleDefinition(
    job=dagster_crawler_agendamento_job,
    cron_schedule="*/20 * * * *",  # every 20 minutes
)

defs = Definitions(
    assets=all_assets,
    schedules=[dagster_crawler_agendamento],
)
