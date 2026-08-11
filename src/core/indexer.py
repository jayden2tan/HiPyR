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
        if file_meta == {}:
            meta.append(
                {
                    "path": str(path),
                    "artist": None,
                    "title": None,
                    "album": None,
                    "track": None,
                    "date": None
                }
            )
        else:
            meta.append(
                {
                    "path": str(path),
                    "artist": file_meta["artist"],
                    "title": file_meta["title"],
                    "album": file_meta["album"],
                    "track": file_meta["tracknumber"],
                    "date": file_meta["date"]
                }
            )
    return meta


def encode_json(data):
    with open("index.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def index(paths):
    scanned = scan(paths)
    meta = add_metadata(scanned)
    encode_json(meta)

index(["C:\\Users\\Jay\\Music\\Local Music\\Lift Yr. Skinny Fists Like Antennas to Heaven!"])