from mutagen import File, MutagenError


def get_metadata(file):
    """
    :return: Dictionary with Artist, Track Number, Album, Date, Title
    """
    try:
        audio = File(str(file))
    except OSError, MutagenError:
        audio = {}

    return dict(audio)

