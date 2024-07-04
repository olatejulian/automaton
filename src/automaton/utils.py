import os
import pathlib
import shutil


def file_verify(file_path: str) -> bool:
    return os.path.exists(file_path)


def list_filenames(path: str) -> list[str]:
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


def get_file_extension(filename: str) -> str:
    return pathlib.Path(filename).suffix


def directory_name(path: str) -> str:
    if not os.path.isdir(path):
        raise NotADirectoryException

    return pathlib.Path(path).name


class NotADirectoryException(Exception):
    pass
