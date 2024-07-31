import sqlite3
from pathlib import Path
from typing import TypedDict

import typer

from automaton.modules.pokemon import (
    PokemonService,
    SqliteUnboundNationalPokeDex,
)

from ..commands import AddPokemonsFromCsv, GetPokemons
from ..config import TableConfig


class Commands(TypedDict):
    add_pokemons_from_csv: AddPokemonsFromCsv
    get_pokemons: GetPokemons


class UnboundModule:
    app_name = "automaton/cli/pokemon"
    app_dir = Path(typer.get_app_dir(app_name))
    db_path = str((app_dir / "pokemon.db").absolute())
    table_title = "Pokemon Unbound National PokeDex"
    table_config = TableConfig(title=table_title)
    sqlite_connection = sqlite3.connect(db_path)
    pokedex = SqliteUnboundNationalPokeDex(sqlite_connection)
    service = PokemonService(pokedex)

    commands: Commands = {
        "add_pokemons_from_csv": AddPokemonsFromCsv(service),
        "get_pokemons": GetPokemons(service, table_config),
    }
