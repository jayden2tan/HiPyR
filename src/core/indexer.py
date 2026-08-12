import json
import magic
from pathlib import Path
from utils import metadata


def scan(paths: list):
    """
    might come back implement yield instead of appending to a list for large amounts of files
    """
    file_paths = []
    for path in paths:
        for item in Path(path).rglob("*"):
            if item.is_file():
                try:
                    with open(item, "rb") as i:
                        # reads the first 1445 bytes instead of whole file to speed up processing
                        # https://mimesniff.spec.whatwg.org/#resource-header
                        header = i.read(1445)
                    if magic.from_buffer(header, mime=True).startswith("audio/"):
                        file_paths.append(str(item))
                except OSError:
                    pass

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

