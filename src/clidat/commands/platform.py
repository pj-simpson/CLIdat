import click

from clidat.meta import (
    company_id_required,
    company_id_required_with_pagination,
    pagination,
)

from ..tui.viewer import ViewerDispatcher


@click.command("get-company")
@click.pass_context
@company_id_required
def get_company(ctx: click.Context, company_id: str, json: bool = False):
    client = ctx.obj
    company = client.get_company(company_id)
    company_json = company.json()
    viewer = ViewerDispatcher(data=company_json, json_flag=json)
    viewer()


@click.command("get-companies")
@click.pass_context
@pagination
def get_companies(
    ctx: click.Context,
    page_size: int,
    page_number: int,
    query: str,
    order_by: str,
    json: bool = False,
):
    client = ctx.obj
    companies = client.get_companies_page(
        page_size=page_size, page_number=page_number, query=query, order_by=order_by
    )
    companies_json = companies.json()
    viewer = ViewerDispatcher(data=companies_json, json_flag=json)
    viewer()


@click.command("get-sync-settings")
@click.pass_context
@company_id_required
def get_sync_settings(ctx: click.Context, company_id: str, json: bool = False):
    client = ctx.obj
    sync_settings = client.get_sync_settings(company_id)
    sync_settings_json = sync_settings.json()
    viewer = ViewerDispatcher(data=sync_settings_json, json_flag=json)
    viewer()


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
    json: bool = False,
):
    client = ctx.obj
    connections = client.get_connections_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    connections_json = connections.json()
    viewer = ViewerDispatcher(data=connections_json, json_flag=json)
    viewer()


@click.command("get-connection")
@click.pass_context
@click.option("--connection", required=True, type=str)
@company_id_required
def get_connection(
    ctx: click.Context, company_id: str, connection: str, json: bool = False
):
    client = ctx.obj
    connection_result = client.get_connection(company_id, connection)
    connection_result_json = connection_result.json()
    viewer = ViewerDispatcher(data=connection_result_json, json_flag=json)
    viewer()


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
    json: bool = False,
):
    client = ctx.obj
    datasets = client.get_data_sets_page(
        company_id=company_id,
        page_size=page_size,
        page_number=page_number,
        query=query,
        order_by=order_by,
    )
    datasets_json = datasets.json()
    viewer = ViewerDispatcher(data=datasets_json, json_flag=json)
    viewer()


@click.command("get-dataset")
@click.pass_context
@click.option("--dataset", required=True, type=str)
@company_id_required
def get_dataset(ctx, company_id, dataset, json: bool = False):
    client = ctx.obj
    dataset_result = client.get_data_set(company_id, dataset)
    dataset_result_json = dataset_result.json()
    viewer = ViewerDispatcher(data=dataset_result_json, json_flag=json)
    viewer()


@click.command("get-data-status")
@click.pass_context
@company_id_required
def get_data_status(ctx: click.Context, company_id: str, json: bool = False):
    client = ctx.obj
    data_status = client.get_data_status(company_id)
    data_status_json = data_status.json()
    viewer = ViewerDispatcher(data=data_status_json, json_flag=json)
    viewer()
