import click
from pycompanydata import Codat
from pyfx import PyfxApp

from clidat.auth import get_token
from clidat.meta import company_id_required, pagination


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
    company = client.get_companies_page(
        page_size=page_size, page_number=page_number, query=query, order_by=order_by
    )
    PyfxApp(data=company).run()
