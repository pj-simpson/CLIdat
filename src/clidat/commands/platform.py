import click
from pyfx import PyfxApp

from clidat.meta import (
    company_id_required,
    company_id_required_with_pagination,
    pagination,
)


@click.command("get-company")
@click.pass_context
@company_id_required
def get_company(ctx: click.Context, company_id: str):
    client = ctx.obj
    company = client.get_company(company_id)
    PyfxApp(data=company).run()


@click.command("get-companies")
@click.pass_context
@pagination
def get_companies(
    ctx: click.Context,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    companies = client.get_companies_page(
        page_size=page_size, page_number=page_number, query=query, order_by=order_by
    )
    PyfxApp(data=companies).run()


@click.command("get-sync-settings")
@click.pass_context
@company_id_required
def get_sync_settings(ctx: click.Context, company_id: str):
    client = ctx.obj
    sync_settings = client.get_sync_settings(company_id)
    PyfxApp(data=sync_settings).run()


@click.command("get-connections")
@click.pass_context
@company_id_required_with_pagination
def get_connections(
    ctx: click.Context,
    company_id: str,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    connections = client.get_connections_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=connections).run()


@click.command("get-connection")
@click.pass_context
@click.option("--connection", required=True, type=str)
@company_id_required
def get_connection(ctx: click.Context, company_id: str, connection: str):
    client = ctx.obj
    connection_result = client.get_connection(company_id, connection)
    PyfxApp(data=connection_result).run()


@click.command("get-datasets")
@click.pass_context
@company_id_required_with_pagination
def get_datasets(
    ctx: click.Context,
    company_id: str,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
):
    client = ctx.obj
    datasets = client.get_data_sets_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    PyfxApp(data=datasets).run()


@click.command("get-dataset")
@click.pass_context
@click.option("--dataset", required=True, type=str)
@company_id_required
def get_dataset(ctx, company_id, dataset):
    client = ctx.obj
    dataset_result = client.get_data_set(company_id, dataset)
    PyfxApp(data=dataset_result).run()


@click.command("get-data-status")
@click.pass_context
@company_id_required
def get_data_status(ctx: click.Context, company_id: str):
    client = ctx.obj
    dataset = client.get_data_status(company_id)
    PyfxApp(data=dataset).run()
