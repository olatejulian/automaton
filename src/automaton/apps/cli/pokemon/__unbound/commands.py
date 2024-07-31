import sqlite3

from automaton.apps.cli.table import ConsoleTable
from automaton.modules import text

from .. import constants


def __color_type(type_: str):
    return constants.POKEMON_TYPES_COLORS[type_]


def __db():
    return sqlite3.connect(constants.DB_PATH)


def __is_table_exists():
    with __db() as connection:
        return bool(
            connection.cursor()
            .execute(
                """
                SELECT
                    name
                FROM
                    sqlite_master
                WHERE
                    type='table' AND name='pokemon_unbound_national_pokedex';
                """
            )
            .fetchone()
        )


def create_table(csv_path: str):
    data = list(text.Text.read_csv(csv_path))

    del data[0]

    with __db() as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS
                pokemon_unbound_national_pokedex (
                    dex_num INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    type_01 TEXT NOT NULL,
                    type_02 TEXT NOT NULL,
                    hp INTEGER NOT NULL,
                    attack INTEGER NOT NULL,
                    defense INTEGER NOT NULL,
                    sp_attack INTEGER NOT NULL,
                    sp_defense INTEGER NOT NULL,
                    speed INTEGER NOT NULL,
                    total INTEGER NOT NULL
                );
            """
        )

        cursor.executemany(
            """
            INSERT OR REPLACE INTO
                pokemon_unbound_national_pokedex
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            data,
        )


def get(query: str):
    with __db() as connection:
        rows = []
        for row in (
            connection.cursor()
            .execute(
                f"SELECT * FROM pokemon_unbound_national_pokedex {query};"
            )
            .fetchall()
        ):
            (
                dex_num,
                name,
                type_01,
                type_02,
                hp,
                attack,
                defense,
                sp_attack,
                sp_defense,
                speed,
                total,
            ) = row

            rows.append(
                [
                    str(value)
                    for value in [
                        dex_num,
                        name,
                        ConsoleTable.colored_value(
                            __color_type(type_01), type_01
                        ),
                        ConsoleTable.colored_value(
                            __color_type(type_02), type_02
                        ),
                        hp,
                        attack,
                        defense,
                        sp_attack,
                        sp_defense,
                        speed,
                        total,
                    ]
                ]
            )

    table = ConsoleTable(
        "Pokemon Unbound National Pokedex",
        [
            "dex_num",
            "name",
            "type_01",
            "type_02",
            "hp",
            "attack",
            "defense",
            "sp_attack",
            "sp_defense",
            "speed",
            "total",
        ],
        rows,
    )

    table.show()
