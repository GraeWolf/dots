#!/bin/sh

rm /tmp/screenshot.png
scrot /tmp/screenshot.png
convert /tmp/screenshot.png -blur 0x20 /tmp/screenlock.png
i3lock -i /tmp/screenlock.png
