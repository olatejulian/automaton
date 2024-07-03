import os


def file_verify(file_path: str) -> bool:
    return os.path.exists(file_path)
