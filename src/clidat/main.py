import os

import click
from pycompanydata import Codat

from clidat.auth import auth, get_token
from clidat.commands.accounting import (
    get_account,
    get_account_transaction,
    get_account_transactions,
    get_accounts,
    get_bill,
    get_bills,
    get_invoice,
    get_invoices,
    get_payment,
    get_payments,
    get_supplier,
    get_suppliers,
)
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
@click.pass_context
def cli(ctx: click.Context):
    if os.path.exists("ct.db"):
        credentials = get_token()
        client = Codat(credentials)
        ctx.obj = client


cli.add_command(auth)
cli.add_command(get_company)
cli.add_command(get_companies)
cli.add_command(get_sync_settings)
cli.add_command(get_connections)
cli.add_command(get_connection)
cli.add_command(get_datasets)
cli.add_command(get_dataset)
cli.add_command(get_data_status)
cli.add_command(get_invoices)
cli.add_command(get_invoice)
cli.add_command(get_supplier)
cli.add_command(get_suppliers)
cli.add_command(get_accounts)
cli.add_command(get_account)
cli.add_command(get_account_transactions)
cli.add_command(get_account_transaction)
cli.add_command(get_bills)
cli.add_command(get_bill)
cli.add_command(get_payments)
cli.add_command(get_payment)


if __name__ == "__main__":
    cli()
