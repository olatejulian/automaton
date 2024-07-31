from typer import Typer

from automaton.apps.cli import common

from . import commands

unbound = Typer(name="unbound")


@unbound.command()
def create_table(csv_path: str):
    common.try_run(commands.create_table, csv_path=csv_path)


@unbound.command()
def get(query: str):
    common.try_run(commands.get, query=query)
