import errno
import os
import pickle

import click


@click.command()
@click.option(
    "--credentials",
    prompt="Your Codat API Key:",
    hide_input=True,
    help="Codat credentials",
)
def auth(credentials: str):
    # start afresh every time we persist a token. We only ever want one.
    if os.path.exists("ct.db"):
        os.remove("ct.db")

    with open("ct.db", "wb") as db:
        pickle.dump(credentials, db, pickle.HIGHEST_PROTOCOL)

    click.echo("Codat Token Saved Successfully")


def get_token():
    if os.path.exists("ct.db"):
        with open("ct.db", "rb") as token:
            return pickle.load(token)
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), "ct.db")
