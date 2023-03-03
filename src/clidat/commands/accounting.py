import click
from pycompanydata import Codat
from pyfx import PyfxApp

from clidat.auth import get_token
from clidat.meta import (
    company_and_connection_ids_required,
    company_id__and_connection_required_with_pagination,
    company_id_required,
    company_id_required_with_pagination,
    pagination,
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


@click.command("get-account_transaction")
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
def get_account(company_id, bill):
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
def get_account(company_id, supplier):
    credentials = get_token()
    client = Codat(credentials)
    supplier_result = client.get_supplier(company_id, supplier)
    PyfxApp(data=supplier_result).run()


# def get_invoices_page(
#         self,
#         company_id: str,
#         page_number: int = 1,
#         page_size: int = 100,
#         query: str = None,
#         order_by: str = None,
# ) -> PaginatedResponse[Invoice]:
#     """Gets a page of invoices for a company
#     :param company_id: Unique identifier for a company
#     :type company_id: str
#     :param query: Query to pass to Codat API to filter results
#     :type query: str
#     :param order_by: Name of the field to order the results by.
#         Defaults to ascending; prefix with `-` to sort in descending order.
#     :type orderby: str
#     :param page_number: Page number to retrieve.  Default: 1
#     :type page_number: int
#     :param page_size: Number of records to retrieve.  Default: 100
#     :type page_size: int
#     :return: A page of invoices
#     :rtype: PaginatedResponse[Invoice]
#     """
#     invoice_handler = InvoicesHandler(self.key, self.env)
#     return invoice_handler.get_pageof_invoices(
#         company_id, page_number, page_size, query, order_by
#     )
#
#
# def get_invoice(self, company_id: str, invoice_id: str) -> Invoice:
#     """Gets an invoice (by ID) for a company
#     :param company_id: Unique identifier for a company
#     :type company_id: str
#     :param invoice_id: Unique identifier for the invoice
#     :type invoice_id: str
#     :return: An invoice
#     :rtype: Invoice
#     """
#     invoice_handler = InvoicesHandler(self.key, self.env)
#     return invoice_handler.get_single_invoice(company_id, invoice_id)
#
#

#
#
# def get_payment_page(
#         self,
#         company_id: str,
#         page_number: int = 1,
#         page_size: int = 100,
#         query: str = None,
#         order_by: str = None,
# ) -> PaginatedResponse[Payment]:
#     """ """
#     payments_handler = PaymentsHandler(self.key, self.env)
#     return payments_handler.get_page_of_payments(
#         company_id, page_number, page_size, query, order_by
#     )
#
#
# def get_payment(self, company_id: str, payment_id: str) -> Payment:
#     """ """
#     payments_handler = PaymentsHandler(self.key, self.env)
#     return payments_handler.get_single_payment(company_id, payment_id)
