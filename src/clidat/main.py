import click

from clidat.auth import auth
from clidat.commands.platform import (
    get_companies,
    get_company,
    get_connection,
    get_connections,
    get_data_status,
    get_dataset,
    get_datasets,
    get_sync_settings,
)


@click.group()
def cli():
    pass


cli.add_command(auth)
cli.add_command(get_company)
cli.add_command(get_companies)
cli.add_command(get_sync_settings)
cli.add_command(get_connections)
cli.add_command(get_connection)
cli.add_command(get_datasets)
cli.add_command(get_dataset)
cli.add_command(get_data_status)

if __name__ == "__main__":
    cli()
