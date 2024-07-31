from rich.console import Console
from rich.table import Table


class ConsoleTable:
    def __init__(
        self,
        title: str,
        columns: list[str],
        data: list[list[str | None]],
    ):
        self.__table = Table(*columns, title=title)

        for row in data:
            self.__table.add_row(*row)

        self.__console = Console()

    @staticmethod
    def colored_value(color: str, value: str):
        return f"[{color}]{value}[/{color}]"

    def show(self):
        self.__console.print(self.__table)
