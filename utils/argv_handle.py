import os
from pathlib import Path
from config import CONFIG
from utils.check_path import check_path
from utils.get_this_wal import get_this_wal
from utils.replace_in_file import replace_in_file

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

    if action == "prev" or action == "next":
        wallpaper_dir = check_path(CONFIG.wallpapers_dir)
        wallpaper_config_file = check_path(CONFIG.wal_cfg_file)
        this_wallpaper = get_this_wal(Path(CONFIG.wal_cfg_file).parent)

        wallpapers = os.listdir(wallpaper_dir)
        filted_walls = [];
        for i in wallpapers:
            for c in CONFIG.wallpapers:
                if str(i).endswith(c):
                    filted_walls.append(i)

        wallpapers = filted_walls
        for i in range(0, len(wallpapers)):
            wallpapers[i] = str(Path(wallpaper_dir) / wallpapers[i])

        this_wall_index = -1
        try: this_wall_index = wallpapers.index(this_wallpaper)
        except ValueError: this_wall_index = -1

        if action == "prev":
            if this_wall_index <= 0:
                this_wall_index = len(wallpapers) - 1
            else:
                this_wall_index -= 1
        if action == "next":
            if this_wall_index >= len(wallpapers) - 1: this_wall_index = 0
            else: this_wall_index += 1

        replace_in_file(wallpaper_config_file, this_wallpaper, wallpapers[this_wall_index])
        with open(Path(CONFIG.wal_cfg_file).parent / ".this_wal", "w") as f:
            f.write(wallpapers[this_wall_index])
        # print(this_wall_index)
        return
