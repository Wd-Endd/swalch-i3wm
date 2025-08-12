from utils.path_handle import path_handle


class CONFIG:
    # NOTE: The path must be a absolute path or path start with ~/ ($HOME)
    wal_cfg_file = path_handle("~/.config/i3/wallpaper-launch.sh")
    wallpapers_dir = path_handle("~/.wallpaper/")
    wallpapers = [".jpeg", ".jpg", ".g"]
