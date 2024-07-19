from typer import Typer

from .series.cli import series

cli = Typer()

cli.add_typer(series)
