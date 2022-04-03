from libqtile import bar, widget

from colors import nord


bar1 = bar.Bar([
    widget.GroupBox(
        fontsize = 14,
        active = nord['pink'],
        inactive = nord['grey'],
        highlight_method = "border",
        this_current_screen_border = nord['green'],
        this_screen_border = nord['blue'],
        foreground = nord['blue'],
        background = nord['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize = 14,
        foreground = nord['orange'],
        background = nord['bg'],
        padding = 5),
    widget.CurrentLayout(
        fontsize = 14,
        foreground = nord['yellow'],
        background = nord['bg'],
        padding =5),
    widget.TextBox(
        fontaize = 14,
        text="🕪",
        padding = 6,
        foreground = nord['green'],
        background = nord['bg']),
    widget.Volume(
        fontsize = 14,
        foreground = nord['green'],
        background = nord['bg'],),
    widget.Clock(
        fontsize = 14,
        foreground = nord['blue'],
        background = nord['bg'],
        format="%A, %B %d  - "),
    widget.Clock(
        fontsize = 14,
        foreground = nord['red'],
        background = nord['bg'],
        format="%H:%M"),
    #widget.Sep(
    #    linewidth = 0,
    #    padding = 5,
    #    background = nord['bg'],),
    
    ],

    margin=[10, 10, 5, 10],
    opacity = 1,
    size = 25
)

bar2 = bar.Bar([
    widget.GroupBox(
        fontsize = 14,
        active = nord['pink'],
        inactive = nord['grey'],
        highlight_method = "border",
        this_current_screen_border = nord['green'],
        this_screen_border = nord['blue'],
        foreground = nord['blue'],
        background = nord['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize = 14,
        foreground = nord['orange'],
        background = nord['bg'],
        padding = 5),
    widget.CurrentLayout(
        fontsize = 14,
        foreground = nord['yellow'],
        background = nord['bg'],
        padding =5),
    widget.TextBox(
        fontaize = 14,
        text="🕪",
        padding = 6,
        foreground = nord['green'],
        background = nord['bg']),
    widget.Volume(
        fontsize = 14,
        foreground = nord['green'],
        background = nord['bg'],),
    widget.Clock(
        fontsize = 14,
        foreground = nord['blue'],
        background = nord['bg'],
        format="%A, %B %d  - "),
    widget.Clock(
        fontsize = 14,
        foreground = nord['red'],
        background = nord['bg'],
        format="%H:%M"),
    widget.LaunchBar(progs=[
        ('⏾', 'systemctl suspend', 'put computer to sleep')],
        fontsize = 14,
        foreground = nord['white'],
        background = nord['bg'],
        padding = 5,
        #default_icon='/usr/share/icons/Adwaita/24x24/status/night-light-symbolic.symbolic.png'
        ),
    #widget.Sep(
    #    linewidth = 0,
    #    padding = 5,
    #    background = nord['bg'],),
    widget.Systray(
        background = nord['bg'],
        padding = 5),
    
    ],

    margin=[10, 10, 5, 10],
    opacity = 1,
    size = 25
)

