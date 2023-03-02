import click

from clidat.auth import auth
from clidat.commands import get_companies, get_company


@click.group()
def cli():
    pass


cli.add_command(auth)
cli.add_command(get_company)
cli.add_command(get_companies)

if __name__ == "__main__":
    cli()
