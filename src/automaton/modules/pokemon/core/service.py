from ...text import Text
from .pokedex import PokeDex, Query
from .factory import PokemonFactory


class PokemonService:
    def __init__(self, pokedex: PokeDex):
        self.__pokedex = pokedex

    def add_from_csv(self, file_path: str):
        pokemon_matrix = Text.read_csv(file_path)

        pokemons = list(
            map(
                lambda pokemon: self.__pokedex.add(
                    PokemonFactory.create_from_list(pokemon)
                ),
                pokemon_matrix,
            )
        )

        self.__pokedex.add_many(pokemons)

    def get_many(self, query: Query):
        return self.__pokedex.get_many(query)
