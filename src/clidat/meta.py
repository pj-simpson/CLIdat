import functools
from typing import Callable

import click


def company_id_required(func: Callable):
    @functools.wraps(func)
    @click.option("--company-id", "-id", required=True, type=str)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def pagination(func: Callable):
    @functools.wraps(func)
    @click.option("--page-number", required=False, type=int)
    @click.option("--page-size", required=False, type=int)
    @click.option("--query", "-q", required=False, type=str)
    @click.option("--order-by", required=False, type=str)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
