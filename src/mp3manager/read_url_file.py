import validators

from .file_verify import file_verify


class Lines:
    def __init__(self, urls: list[str], not_urls: list[str]):
        self.__urls = urls
        self.__not_urls = not_urls

    def urls_count(self) -> int:
        return len(self.urls)

    def not_urls_count(self) -> int:
        return len(self.not_urls)

    @property
    def urls(self) -> list[str]:
        return self.__urls

    @property
    def not_urls(self) -> list[str]:
        return self.__not_urls


def read_plaintext_url_file(file_path: str) -> Lines:
    if not file_verify(file_path):
        raise FileNotFoundError

    with open(file_path, "r", encoding="utf-8") as file:
        urls = []

        not_urls = []

        while True:
            if line := file.readline():

                striped_line = line.strip()

                if validators.url(striped_line):
                    urls.append(striped_line)

                else:
                    not_urls.append(line)

            else:
                break

        return Lines(urls, not_urls)
