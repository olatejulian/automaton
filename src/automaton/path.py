import os
import shutil
from pathlib import Path


def verify_path(path: str) -> bool:
    return os.path.exists(path)


def list_files(path: str) -> list[str]:
    return [
        f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
    ]


def list_subdirectories(path: str) -> list[str]:
    return [
        f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))
    ]


def rename_file(path: str, old_name: str, new_name: str) -> str:
    return shutil.move(
        os.path.join(path, old_name),
        os.path.join(path, new_name),
    )


def get_file_extension(path: str) -> str:
    if not os.path.isfile(path):
        raise NotAFileException

    return Path(path).suffix


def directory_name(path: str) -> str:
    if not os.path.isdir(path):
        raise NotADirectoryException

    return Path(path).name


def file_name(path: str) -> str:
    if not os.path.isfile(path):
        raise NotAFileException

    return Path(path).stem


class NotADirectoryException(Exception):
    pass


class NotAFileException(Exception):
    pass
