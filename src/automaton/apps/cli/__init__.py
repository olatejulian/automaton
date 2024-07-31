from typer import Typer

from .pokemon.cli import pokemon
from .series.cli import series

cli = Typer()

cli.add_typer(series)

cli.add_typer(pokemon)
