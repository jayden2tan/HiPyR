from mutagen import File


def main(file):
    """
    Get the metadata of a file.

    :return: Release Date, ALbum, Artist, Track Number, Title
    """
    return File(file)