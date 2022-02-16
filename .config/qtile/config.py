#### Graewolf Custom Qtile Config ####
import os
import re
import socket
import subprocess

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.config import Match

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "control"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -modi drun -show drun")),
    Key([mod, "shift"], "Return", lazy.spawn("thunar")),
]

#### BAR COLORS ####

def init_colors():
    return [["#2e3440", "#2e3440"], # 0 panel bg dark grey
            ["#4c566a", "#4c566a"], # 1 grey
            ["#d8dee9", "#d8dee9"], # 2 bt-alt light-grey
            ["#8fbccb", "#8fbccb"], # 3 cyan
            ["#5e81ac", "#5e81ac"], # 4 blue
            ["#b48ead", "#b48ead"], # 5 pink
            ["#a3be8c", "#a3be8c"], # 6 green
            ["#ebcb8b", "#ebcb8b"], # 7 yellow
            ["#d08770", "#d08779"], # 8 orange
            ["#bf616a", "#bf616a"]] # 9 red

#### GROUPS ####

def init_group_names():
    return [("1:", {'layout': 'monadtall'}),
            ("2:", {'layout': 'monadtall', 'matches':[Match(wm_class=["firefox","vivaldi-stable"])]}),
            ("3:", {'layout': 'floating', 'matches':[Match(wm_class=["bitwarden", "steam", "lutris"])]}),
            ("4:", {'layout': 'monadwide', 'matches':[Match(wm_class=["tenacity"])]}),
            ("5:", {'layout': 'monadtall', 'matches':[Match(wm_class=["geary"])]}),
            ("6:", {'layout': 'monadtall'}),
            ("7:", {'layout': 'monadtall'}),
            ("8:", {'layout': 'monadtall'}),
            ("9:", {'layout': 'monadtall'})]


def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))  # Send current window to another group


#### LAYOUTS ####

def init_layout_theme():
    return {"border_width": 2,
            "margin": 6,
            "border_focus": colors[9],
            "border_normal": colors[3]
           }

def init_layouts():
    return [layout.MonadTall(**layout_theme),
            layout.MonadWide(**layout_theme),
            layout.Bsp(**layout_theme),
            layout.Matrix(**layout_theme),
            layout.RatioTile(**layout_theme),
            layout.Floating(border_focus="#3B4022")]

def init_widgets_defaults():
    return dict(font='sans',
                fontsize=20,
                padding=3,
                background = colors[2])

def init_widgets_list():
    widgets_list = [
                widget.GroupBox(
                        visible_groups=['1:', '2:', '3:', '4:','5:', '6:', '7:', '8:', '9:',],
                        fontsize = 20,
                        active = colors[5],
                        inactive = colors[1],
                        highlight_method = "border",
                        this_current_screen_border = colors[6],
                        this_screen_border = colors [4],
                        foreground = colors[4],
                        background = colors[0]),
                widget.Prompt(),
                widget.WindowName(
                        fontsize = 20,
                        foreground = colors[8],
                        background = colors[0],
                        padding = 5),
                widget.CurrentLayout(
                        fontsize = 20,
                        foreground = colors[7],
                        background = colors[0],
                        padding =5),
                widget.TextBox(
                        fontaize = 20,
                        text="🕪",
                        padding = 6,
                        foreground = colors[6],
                        background = colors[0]),
                widget.Volume(
                        fontsize = 20,
                        foreground = colors[6],
                        background = colors[0],),
                #widget.TextBox(
                #        text="⟳",
                #        foreground = colors[2],
                #        background = colors[0]),
                #widget.Pacman(
                #        update_interval = 1800,
                #        foreground = colors[2],
                #        background = colors[0]),
                widget.Clock(
                        fontsize = 20,
                        foreground = colors[4],
                        background = colors[0],
                        format="%A, %B %d - %H:%M"),
                widget.LaunchBar(progs=[
                        ('⏾', 'systemctl suspend', 'put computer to sleep')],
                        fontsize = 20,
                        foreground = colors[9],
                        background = colors[0],
                        padding = 5,
                        #default_icon='/usr/share/icons/Adwaita/24x24/status/night-light-symbolic.symbolic.png'
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        background = colors[0],
                        ),
                widget.Systray(
                        background = colors[0],
                        padding = 5),
                    ]
    return widgets_list

#### SCREENS ####

def init_widgets_screen():
        widgets_screen = init_widgets_list()
        return widgets_screen

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=0.95, size=32))]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

colors = init_colors()
screens = init_screens()
widgets_screen = init_widgets_screen()
widget_defaults = init_widgets_defaults()
widgets_list = init_widgets_list()
layout_theme = init_layout_theme()
layouts = init_layouts()

#### Autostart of Startup Apps ####
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/bin/autostart.sh')
    subprocess.call(['sh', home])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
