from pathlib import Path
import os

this_wal = "%%THIS_WALLPAPER%%"


def get_this_wal(wal_dir):
    this_path = Path(wal_dir) / ".this_wal"
    if os.path.exists(this_path):
        with open(this_path, "r") as f:
            return f.read()
    else:
        with open(this_path, "w") as f:
            f.write(this_wal)
            return this_wal
