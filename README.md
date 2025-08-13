
# swalch-i3

Swalch is a personal project to Make Wallpaper Switch script for I3 Window Manager.

## Preview

You can make a Key Shortcut to run this script

![Video.gif](https://github.com/Wd-Endd/swalch-i3wm/raw/refs/heads/main/.preview/2025_08_13_07_14_40.gif)

## Setup & Usage

To install ``swalch-i3``, follow the tutorial below.

### Depends, Prepare

Some prepare to setup ``swalch``.

1. Your Window Manager is ``i3wm`` or ``sway``.
2. ``git`` command (recommend)
3. You must make sure there is no problem restarting i3wm

### Setup

1. Go to appropriate directory for setup.
2. Clone this repo and open it, command:
```Bash
git clone https://github.com/Wd-Endd/swalch-i3wm.git

cd ./swalch-i3wm
```
3. Edit ``config.py``
```Python
from utils.path_handle import path_handle

class CONFIG:
    # NOTE: The path must be a absolute path or path start with ~/ ($HOME)
    wal_cfg_file = path_handle("~/your/wallpaper/lancher/file")
    wallpapers_dir = path_handle("~/your/wallpaper/dir/")
    wallpapers = [".jpeg", ".jpg", ".png"]
```
4. Reconfigure Your wallpaper launch (First time)
You must You need to reconfigure the launcher wallpaper file. Ex:
```Bash
#!/usr/bin/env bash
#wallpaper_launcher.sh

killall -q xwallpaper
xwallpaper --daemon --stretch \
    # "~/path/to/your/wallpaper"        # replace this line with:
    "%%THIS_WALLPAPER%%"
```
5. Make a shortcut and keybind to run the script
Ex:
```sh
#!/usr/bin/env bash
# ~/.config/i3/swalch

exec python ~/.local/opt/swalch-i3wm/main.py $@

```
```sh
# ~/.config/i3/config
# ...

bindsym $mod+bracketright exec "~/.config/i3/swalch next"; restart
bindsym $mod+bracketleft exec "~/.config/i3/swalch prev"; restart

#...
```
Done, enjoy it?!        ... No animation -_-

## Thanks for see it <3
