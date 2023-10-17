#### Graewolf Custom Qtile Config ####
import os
import re
import socket
import subprocess

from typing import List  # noqa: F401

from libqtile import layout, widget, hook
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.layout.floating import Floating
from libqtile.command import lazy

from colors import dracula
from custom_bar import bar1, bar2, bar3
from Xlib import display as xdisplay



mod = "mod4"
terminal = "wezterm"


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Maximize window for gaming
    Key([mod, "shift"], "m", lazy.window.toggle_fullscreen()),
    
    # Scratchpad keys
    Key([mod, "control"], "Return", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([], "F12", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
]

groups = [
    Group("1", label=" ", layout = 'bsp'),
    Group("2", label=" ", layout = 'monadtall', matches = [Match(wm_class=["firefox"])] ),
    Group("3", label=" ", layout = 'floating', matches = [Match(wm_class=["steam", "lutris"])]),
    Group("4", label=" ", layout = 'monadwide', matches = [Match(wm_class=["audacity"])]),
    Group("5", label=" ", layout = 'monadtall', matches = [Match(wm_class=["geary"])]),
    Group("6", label=" ", layout = 'monadtall'),
    Group("7", label=" ", layout = 'monadtall'),
    Group("8", label=" ", layout = 'columns', matches = [Match(wm_class=["code - oss"])]),
    Group("9", label=" ", layout = 'monadtall', matches = [Match(wm_class=["Spotify"])]),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])
    
groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'alacritty', width=0.6, height=0.5, x=0.2, y=0.1, opacity=1),
    DropDown('mixer', 'pavucontrol', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('bitwarden', 'bitwarden-desktop',
             width=0.5, height=0.6, x=0.3, y=0.1, opacity=1),
]))

#### LAYOUTS ####

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": dracula['red'],
                "border_normal": dracula['cyan'],
            }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Columns(**layout_theme, num_columns = 4),
    layout.Floating(**layout_theme,
                        float_rules=[
                            *Floating.default_float_rules,
                            Match(wm_class="pavucontrol"),
                            Match(wm_class="bitwarden"),
                            ])
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

widget_defaults = dict(
    font='TerminessTTF Nerd Font',
    fontsize=14,
    padding=5,
    foreground=dracula['bg'],
)

extension_defaults = widget_defaults.copy()


                    
#### SCREENS ####

def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        print(screen)
        resources = screen.root.xrandr_get_screen_resources()
        print(resources)

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

num_monitors = get_num_monitors()


screens = [Screen(top=bar1)]

if num_monitors > 1:
    for m in range(num_monitors - 1):
        screens.append(Screen(top=bar2))
            
            
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


#### Autostart of Startup Apps ####
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.call(['sh', home])



