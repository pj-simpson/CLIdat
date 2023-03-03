import click
from pycompanydata import Codat
from pyfx import PyfxApp

from clidat.auth import get_token
from clidat.meta import (
    company_id_required,
    company_id_required_with_pagination,
    pagination,
)


@click.command("get-company")
@company_id_required
def get_company(company_id):
    credentials = get_token()
    client = Codat(credentials)
    company = client.get_company(company_id)
    PyfxApp(data=company).run()


@click.command("get-companies")
@pagination
def get_companies(page_size, page_number, query, order_by):
    credentials = get_token()
    client = Codat(credentials)
    companies = client.get_companies_page(
        page_size=page_size, page_number=page_number, query=query, order_by=order_by
    )
    PyfxApp(data=companies).run()


@click.command("get-sync-settings")
@company_id_required
def get_sync_settings(company_id):
    credentials = get_token()
    client = Codat(credentials)
    sync_settings = client.get_sync_settings(company_id)
    PyfxApp(data=sync_settings).run()


@click.command("get-connections")
@company_id_required_with_pagination
def get_connections(company_id, page_size, page_number, query, order_by):
    credentials = get_token()
    client = Codat(credentials)
    connections = client.get_connections_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=connections).run()


@click.command("get-connection")
@click.option("--connection", required=True, type=str)
@company_id_required
def get_connection(company_id, connection):
    credentials = get_token()
    client = Codat(credentials)
    connection_result = client.get_connection(company_id, connection)
    PyfxApp(data=connection_result).run()


@click.command("get-datasets")
@company_id_required_with_pagination
def get_datasets(company_id, page_size, page_number, query, order_by):
    credentials = get_token()
    client = Codat(credentials)
    datasets = client.get_data_sets(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=datasets).run()


@click.command("get-dataset")
@click.option("--dataset", required=True, type=str)
@company_id_required
def get_dataset(company_id, dataset):
    credentials = get_token()
    client = Codat(credentials)
    dataset_result = client.get_data_set(company_id, dataset)
    PyfxApp(data=dataset_result).run()


@click.command("get-data-status")
@company_id_required
def get_data_status(company_id):
    credentials = get_token()
    client = Codat(credentials)
    dataset = client.get_data_status(company_id)
    PyfxApp(data=dataset).run()
