import sys
from typing import Optional

from rich.console import Console
from typer import Typer

pdf = Typer(name="pdf")

console_err = Console(stderr=True)


@pdf.command()
def set_title(new_title: Optional[str] = None):
    try:
        print(new_title)

        sys.exit(0)

    except Exception as e:
        console_err.print(e)

        sys.exit(1)
