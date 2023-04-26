import click

from clidat.meta import (
    company_and_connection_ids_required,
    company_id__and_connection_required_with_pagination,
    company_id_required,
    company_id_required_with_pagination,
)

from ..tui.viewer import ViewerDispatcher


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
    json: bool = False,
):
    client = ctx.obj
    accounts = client.get_accounts_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    accounts_json = accounts.json()
    viewer = ViewerDispatcher(
        data=accounts_json, json_flag=json, data_type="Chart of Accounts"
    )
    viewer()


@click.command("get-account")
@click.pass_context
@click.option("--account", required=True, type=str)
@company_id_required
def get_account(ctx: click.Context, company_id: str, account: str, json: bool = False):
    client = ctx.obj
    account_result = client.get_account(company_id, account)
    account_result_json = account_result.json()
    viewer = ViewerDispatcher(
        data=account_result_json, json_flag=json, data_type="Accounts"
    )
    viewer()


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
    json: bool = False,
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
    account_transactions_json = account_transactions.json()
    viewer = ViewerDispatcher(
        data=account_transactions_json,
        json_flag=json,
        data_type="List of Account Transactions",
    )
    viewer()


@click.command("get-account-transaction")
@click.pass_context
@click.option("--account-transaction", required=True, type=str)
@company_and_connection_ids_required
def get_account_transaction(
    ctx: click.Context,
    company_id: str,
    connection: str,
    account_transaction: str,
    json: bool = False,
):
    client = ctx.obj
    account_transaction_result = client.get_account_transaction(
        company_id, connection, account_transaction
    )
    account_transaction_result_json = account_transaction_result.json()
    viewer = ViewerDispatcher(
        data=account_transaction_result_json,
        json_flag=json,
        data_type="Account Transaction",
    )
    viewer()


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
    json: bool = False,
):
    client = ctx.obj
    bills = client.get_bills_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    bills_json = bills.json()
    viewer = ViewerDispatcher(
        data=bills_json, json_flag=json, data_type="List of Bills"
    )
    viewer()


@click.command("get-bill")
@click.pass_context
@click.option("--bill", required=True, type=str)
@company_id_required
def get_bill(ctx: click.Context, company_id: str, bill: str, json: bool = False):
    client = ctx.obj
    bill_result = client.get_bill(company_id, bill)
    bill_result_json = bill_result.json()
    viewer = ViewerDispatcher(data=bill_result_json, json_flag=json, data_type="Bills")
    viewer()


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
    json: bool = False,
):
    client = ctx.obj
    suppliers = client.get_suppliers_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    suppliers_json = suppliers.json()
    viewer = ViewerDispatcher(
        data=suppliers_json, json_flag=json, data_type="List of Suppliers"
    )
    viewer()


@click.command("get-supplier")
@click.pass_context
@click.option("--supplier", required=True, type=str)
@company_id_required
def get_supplier(
    ctx: click.Context, company_id: str, supplier: str, json: bool = False
):
    client = ctx.obj
    supplier_result = client.get_supplier(company_id, supplier)
    supplier_result_json = supplier_result.json()
    viewer = ViewerDispatcher(
        data=supplier_result_json, json_flag=json, data_type="Supplier"
    )
    viewer()


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
    json: bool = False,
):
    client = ctx.obj
    invoices = client.get_invoices_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    invoices_json = invoices.json()
    viewer = ViewerDispatcher(
        data=invoices_json, json_flag=json, data_type="List of Invoices"
    )
    viewer()


@click.command("get-invoice")
@click.pass_context
@click.option("--invoice", required=True, type=str)
@company_id_required
def get_invoice(ctx: click.Context, company_id: str, invoice: str, json: bool = False):
    client = ctx.obj
    invoice_result = client.get_invoice(company_id, invoice)
    invoice_result_json = invoice_result.json()
    viewer = ViewerDispatcher(
        data=invoice_result_json, json_flag=json, data_type="Invoice"
    )
    viewer()


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
    json: bool = False,
):
    client = ctx.obj
    payments = client.get_payment_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    payments_json = payments.json()
    viewer = ViewerDispatcher(
        data=payments_json, json_flag=json, data_type="List of Payments"
    )
    viewer()


@click.command("get-payment")
@click.pass_context
@click.option("--payment", required=True, type=str)
@company_id_required
def get_payment(ctx: click.Context, company_id: str, payment: str, json: bool = False):
    client = ctx.obj
    payment_result = client.get_payment(company_id, payment)
    payment_result_json = payment_result.json()
    viewer = ViewerDispatcher(
        data=payment_result_json, json_flag=json, data_type="Payment"
    )
    viewer()
