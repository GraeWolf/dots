#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then

    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then

    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# Screen locking
xset s on
xset s 600
xss-lock ~/.local/bin/securelock lock &

# unlock the keyring
eval "$(/usr/bin/gnome-keyring-daemon --start --components=gpg,ssh,pkcs11,secrets)"
export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK
export SSH_AUTH_SOCK="$GNOME_KEYRING_CONTROL/ssh"

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi


# Launch apps and services
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/polkit-1/polkit-agent-helper-1 &
udiskie -t &
numlockx &
~/.local/bin/securelock &

# Launce WM or DE

dbus-launch qtile start
#dbus-launch leftwm
#dbus-launch startxfce4
#awesome
#xmonad
