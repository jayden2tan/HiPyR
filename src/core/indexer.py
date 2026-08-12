import json
import magic
from pathlib import Path
from utils import metadata


def scan(paths: list):
    """
    works but is kind of slow (~3 ms/file)
    might come back implement yield instead of appending to a list for large amounts of files
    """
    file_paths = []
    for path in paths:
        directory = Path(path)
        for file in directory.iterdir():
            if file.is_file() and magic.from_file(str(file), mime=True).startswith("audio/"):
                file_paths.append(str(file))
                # yield str(file)

    return file_paths


def add_metadata(paths) -> list:
    meta = []
    for path in paths:
        file_meta = metadata.get_metadata(path)
        meta.append(
            {
                "path": str(path),
                "artist": file_meta.get("artist", None),
                "title": file_meta.get("title", None),
                "album": file_meta.get("album", None),
                "track": file_meta.get("tracknumber", None),
                "date": file_meta.get("date", None)
            }
        )
    return meta


def encode_json(data):
    with open("index.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def index(paths):
    encode_json(add_metadata(scan(paths)))

