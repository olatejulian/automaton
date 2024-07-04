from typer import Typer

from .utils import (
    directory_name,
    get_file_extension,
    list_filenames,
    rename_file,
)
from .series import get_season_episode, is_video_file, video_name_format

cli = Typer()


@cli.command()
def rename_series_episodes(path: str) -> None:
    filenames = list_filenames(path)

    for filename in filenames:
        if is_video_file(filename):
            if season_episode := get_season_episode(filename):
                new_name = video_name_format(
                    directory_name(path),
                    season_episode,
                    get_file_extension(filename),
                )

                rename_file(path, filename, new_name)


@cli.command()
def rename_subtitles(path: str) -> None:
    raise NotImplementedError
