import click
from pyfx import PyfxApp

from clidat.meta import (
    company_and_connection_ids_required,
    company_id__and_connection_required_with_pagination,
    company_id_required,
    company_id_required_with_pagination,
)


@click.command("get-accounts")
@click.pass_context
@company_id_required_with_pagination
def get_accounts(
    ctx: click.Context,
    company_id: str,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    accounts = client.get_accounts_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=accounts).run()


@click.command("get-account")
@click.pass_context
@click.option("--account", required=True, type=str)
@company_id_required
def get_account(ctx: click.Context, company_id: str, account: str):
    client = ctx.obj
    account_result = client.get_account(company_id, account)
    PyfxApp(data=account_result).run()


@click.command("get-account-transactions")
@click.pass_context
@company_id__and_connection_required_with_pagination
def get_account_transactions(
    ctx: click.Context,
    company_id: str,
    connection: str,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    account_transactions = client.get_account_transactions_page(
        company_id=company_id,
        connection_id=connection,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=account_transactions).run()


@click.command("get-account-transaction")
@click.pass_context
@click.option("--account-transaction", required=True, type=str)
@company_and_connection_ids_required
def get_account_transaction(
    ctx: click.Context, company_id: str, connection: str, account_transaction: str
):
    client = ctx.obj
    account_transaction_result = client.get_account_transaction(
        company_id, connection, account_transaction
    )
    PyfxApp(data=account_transaction_result).run()


@click.command("get-bills")
@click.pass_context
@company_id_required_with_pagination
def get_bills(
    ctx: click.Context,
    company_id: str,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    bills = client.get_bills_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=bills).run()


@click.command("get-bill")
@click.pass_context
@click.option("--bill", required=True, type=str)
@company_id_required
def get_bill(ctx: click.Context, company_id: str, bill: str):
    client = ctx.obj
    bill_result = client.get_bill(company_id, bill)
    PyfxApp(data=bill_result).run()


@click.command("get-suppliers")
@click.pass_context
@company_id_required_with_pagination
def get_suppliers(
    ctx: click.Context,
    company_id: str,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    suppliers = client.get_suppliers_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=suppliers).run()


@click.command("get-supplier")
@click.pass_context
@click.option("--supplier", required=True, type=str)
@company_id_required
def get_supplier(ctx: click.Context, company_id: str, supplier: str):
    client = ctx.obj
    supplier_result = client.get_supplier(company_id, supplier)
    PyfxApp(data=supplier_result).run()


@click.command("get-invoices")
@click.pass_context
@company_id_required_with_pagination
def get_invoices(
    ctx: click.Context,
    company_id: str,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    invoices = client.get_invoices_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=invoices).run()


@click.command("get-invoice")
@click.pass_context
@click.option("--invoice", required=True, type=str)
@company_id_required
def get_invoice(ctx: click.Context, company_id: str, invoice: str):
    client = ctx.obj
    invoice_result = client.get_invoice(company_id, invoice)
    PyfxApp(data=invoice_result).run()


@click.command("get-payments")
@click.pass_context
@company_id_required_with_pagination
def get_payments(
    ctx: click.Context,
    company_id: str,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    payments = client.get_payment_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=payments).run()


@click.command("get-payment")
@click.pass_context
@click.option("--payment", required=True, type=str)
@company_id_required
def get_payment(ctx: click.Context, company_id: str, payment: str):
    client = ctx.obj
    payment_result = client.get_payment(company_id, payment)
    PyfxApp(data=payment_result).run()
