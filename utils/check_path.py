
import os

from config import CONFIG


def check_path(p):
    if os.path.exists(p):
        return p
    else:
        raise Exception("File/Directory is not exists:", p)
