import os
from pathlib import Path

from config import CONFIG
from utils.check_path import check_path
from utils.get_this_wal import get_this_wal
from utils.path_handle import path_handle


def argv_handle(argv):
    if len(argv) < 1: raise Exception("the action not found. pls type with 'help'.")
    
    action = argv[1]
    if action == "help":
        print("Usage: <command> <action>")
        print("Action:")
        print("  - help: Show how to use the command")
        print("  - config: Get config path")
        print("  - prev: Change previous wallpaper")
        print("  - next: Change next wallpaper")
        return

    if action == "config":
        config_file = Path(__file__).resolve().parent.parent / "config.py"
        print("The config file is in:")
        print(f"  {config_file}")
        return

    if action == ("prev" or "next"):
        wallpaper_dir = check_path(CONFIG.wallpapers_dir)
        wallpaper_config_file = check_path(CONFIG.wal_cfg_file)
        this_wallpaper = get_this_wal(wallpaper_dir)

        wallpapers = os.listdir(wallpaper_dir)
