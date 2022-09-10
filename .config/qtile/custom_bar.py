from libqtile import bar, widget

from colors import dracula


bar1 = bar.Bar([
    widget.GroupBox(
        fontsize = 14,
        active = dracula['pink'],
        inactive = dracula['grey'],
        highlight_method = "border",
        this_current_screen_border = dracula['green'],
        this_screen_border = dracula['blue'],
        foreground = dracula['blue'],
        background = dracula['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize = 14,
        foreground = dracula['orange'],
        background = dracula['bg'],
        padding = 5),
    widget.CurrentLayout(
        fontsize = 14,
        foreground = dracula['yellow'],
        background = dracula['bg'],
        padding =5),
    widget.TextBox(
        fontaize = 14,
        text="",
        padding = 6,
        foreground = dracula['green'],
        background = dracula['bg']),
    widget.Volume(
        fontsize = 14,
        foreground = dracula['green'],
        background = dracula['bg'],),
    widget.Clock(
        fontsize = 14,
        foreground = dracula['blue'],
        background = dracula['bg'],
        format="%A, %B %d  - "),
    widget.Clock(
        fontsize = 14,
        foreground = dracula['red'],
        background = dracula['bg'],
        format="%H:%M"),
    #widget.Sep(
    #    linewidth = 0,
    #    padding = 5,
    #    background = dracula['bg'],),
    
    ],

    margin=[10, 10, 5, 10],
    opacity = 1,
    size = 25
)

bar2 = bar.Bar([
    widget.GroupBox(
        fontsize = 14,
        active = dracula['pink'],
        inactive = dracula['grey'],
        highlight_method = "border",
        this_current_screen_border = dracula['green'],
        this_screen_border = dracula['blue'],
        foreground = dracula['blue'],
        background = dracula['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize = 14,
        foreground = dracula['orange'],
        background = dracula['bg'],
        padding = 5),
    widget.CurrentLayout(
        fontsize = 14,
        foreground = dracula['yellow'],
        background = dracula['bg'],
        padding =5),
    widget.TextBox(
        fontaize = 14,
        text="",
        padding = 6,
        foreground = dracula['green'],
        background = dracula['bg']),
    widget.Volume(
        fontsize = 14,
        foreground = dracula['green'],
        background = dracula['bg'],),
    widget.Clock(
        fontsize = 14,
        foreground = dracula['blue'],
        background = dracula['bg'],
        format="%A, %B %d  - "),
    widget.Clock(
        fontsize = 14,
        foreground = dracula['red'],
        background = dracula['bg'],
        format="%H:%M"),
    widget.LaunchBar(progs=[
        ('⏾', 'systemctl suspend', 'put computer to sleep')],
        fontsize = 14,
        foreground = dracula['white'],
        background = dracula['bg'],
        padding = 5,
        #default_icon='/usr/share/icons/Adwaita/24x24/status/night-light-symbolic.symbolic.png'
        ),
    widget.Sep(
        linewidth = 0,
        padding = 5,
        background = dracula['bg'],),
    widget.Systray(
        background = dracula['bg'],
        padding = 5),
    
    ],

    margin=[10, 10, 5, 10],
    opacity = 1,
    size = 25
)

bar3 = bar.Bar([
    widget.GroupBox(
        fontsize = 14,
        active = dracula['pink'],
        inactive = dracula['grey'],
        highlight_method = "border",
        this_current_screen_border = dracula['green'],
        this_screen_border = dracula['blue'],
        foreground = dracula['blue'],
        background = dracula['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize = 14,
        foreground = dracula['orange'],
        background = dracula['bg'],
        padding = 5),
    widget.CurrentLayout(
        fontsize = 14,
        foreground = dracula['yellow'],
        background = dracula['bg'],
        padding =5),
    widget.Clock(
        fontsize = 14,
        foreground = dracula['red'],
        background = dracula['bg'],
        format="%H:%M"),
    
    ],

    margin=[10, 10, 5, 10],
    opacity = 1,
    size = 25
)

