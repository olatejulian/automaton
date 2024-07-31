from typing import Literal, Optional

from typer import Typer

from automaton.apps.cli import common

from .module import UnboundModule

unbound_cli = Typer(name="unbound")


@unbound_cli.command()
def add_data(path: str, file_format: str = "csv"):
    match file_format:
        case "csv":
            common.try_run(
                UnboundModule.commands["add_pokemons_from_csv"], path=path
            )


@unbound_cli.command()
def get(
    where: Optional[str] = None,
    order_by: Optional[str] = None,
    limit: Optional[int] = None,
):
    common.try_run(
        UnboundModule.commands["get_pokemons"],
        query={"where": where, "order_by": order_by, "limit": limit},
    )
