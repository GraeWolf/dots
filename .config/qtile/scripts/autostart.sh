#! /bin/bash

~/.config/qtile/scripts/locker.sh &
picom --config ~/.config/picom.conf &
~/bin/wallpaper &
nm-applet &
volumeicon &
~/.screenlayout/qtile_layout.sh &
sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &
#megasync &
dropbox start &
pipewire &
