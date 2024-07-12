from typing import Callable, Iterator, TypeVar

T = TypeVar("T")


class Text:
    def __init__(self, text_file_path: str):
        self.__text_path = text_file_path

    def __iter__(self):
        with open(
            file=self.__text_path, mode="r", encoding="utf-8"
        ) as text_file:
            while line := text_file.readline():
                yield line

    def map(self, func: Callable[[str], T]) -> Iterator[T]:
        for line in self:
            yield func(line)

    def filter(self, func: Callable[[str], bool]) -> Iterator[str]:
        for line in self:
            if func(line):
                yield line
