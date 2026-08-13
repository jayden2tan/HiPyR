from mutagen import File


def get_metadata(file):
    """
    :return: Dictionary with Artist, Track Number, Album, Date, Title
    """
    return File(str(file))