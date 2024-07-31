from abc import ABC, abstractmethod
from typing import TypedDict

from .pokemon import Pokemon


class Query(TypedDict):
    where: str | None
    order_by: str | None
    limit: int | None


class PokeDex(ABC):
    @abstractmethod
    def add(self, pokemon: Pokemon):
        raise NotImplementedError

    @abstractmethod
    def add_many(self, pokemons: list[Pokemon]):
        raise NotImplementedError

    @abstractmethod
    def get_many(self, query: Query) -> list[Pokemon]:
        raise NotImplementedError
