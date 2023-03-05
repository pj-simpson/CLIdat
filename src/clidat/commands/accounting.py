import click
from pycompanydata import Codat
from pyfx import PyfxApp

from clidat.auth import get_token
from clidat.meta import (
    company_and_connection_ids_required,
    company_id__and_connection_required_with_pagination,
    company_id_required,
    company_id_required_with_pagination,
)


@click.command("get-accounts")
@company_id_required_with_pagination
def get_accounts(company_id, page_size, page_number, query, order_by):
    credentials = get_token()
    client = Codat(credentials)
    accounts = client.get_accounts_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=accounts).run()


@click.command("get-account")
@click.option("--account", required=True, type=str)
@company_id_required
def get_account(company_id, account):
    credentials = get_token()
    client = Codat(credentials)
    account_result = client.get_account(company_id, account)
    PyfxApp(data=account_result).run()


@click.command("get-account-transactions")
@company_id__and_connection_required_with_pagination
def get_account_transactions(
    company_id, connection, page_size, page_number, query, order_by
):
    credentials = get_token()
    client = Codat(credentials)
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
@click.option("--account-transaction", required=True, type=str)
@company_and_connection_ids_required
def get_account_transaction(company_id, connection, account_transaction):
    credentials = get_token()
    client = Codat(credentials)
    account_transaction_result = client.get_account_transaction(
        company_id, connection, account_transaction
    )
    PyfxApp(data=account_transaction_result).run()


@click.command("get-bills")
@company_id_required_with_pagination
def get_bills(company_id, page_size, page_number, query, order_by):
    credentials = get_token()
    client = Codat(credentials)
    bills = client.get_bills_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=bills).run()


@click.command("get-bill")
@click.option("--bill", required=True, type=str)
@company_id_required
def get_bill(company_id, bill):
    credentials = get_token()
    client = Codat(credentials)
    bill_result = client.get_bill(company_id, bill)
    PyfxApp(data=bill_result).run()


@click.command("get-suppliers")
@company_id_required_with_pagination
def get_suppliers(company_id, page_size, page_number, query, order_by):
    credentials = get_token()
    client = Codat(credentials)
    suppliers = client.get_suppliers_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=suppliers).run()


@click.command("get-supplier")
@click.option("--supplier", required=True, type=str)
@company_id_required
def get_supplier(company_id, supplier):
    credentials = get_token()
    client = Codat(credentials)
    supplier_result = client.get_supplier(company_id, supplier)
    PyfxApp(data=supplier_result).run()


@click.command("get-invoices")
@company_id_required_with_pagination
def get_invoices(company_id, page_size, page_number, query, order_by):
    credentials = get_token()
    client = Codat(credentials)
    invoices = client.get_invoices_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=invoices).run()


@click.command("get-invoice")
@click.option("--invoice", required=True, type=str)
@company_id_required
def get_invoice(company_id, invoice):
    credentials = get_token()
    client = Codat(credentials)
    invoice_result = client.get_invoice(company_id, invoice)
    PyfxApp(data=invoice_result).run()


@click.command("get-payments")
@company_id_required_with_pagination
def get_payments(company_id, page_size, page_number, query, order_by):
    credentials = get_token()
    client = Codat(credentials)
    payments = client.get_payment_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=payments).run()


@click.command("get-payment")
@click.option("--payment", required=True, type=str)
@company_id_required
def get_payment(company_id, payment):
    credentials = get_token()
    client = Codat(credentials)
    payment_result = client.get_payment(company_id, payment)
    PyfxApp(data=payment_result).run()
