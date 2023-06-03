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
    widget.Battery(
        background = dracula['bg'],
        foreground = dracula['magenta'],
        fontsize = 14,
        format = '{char}{percent:2.0%}',
        low_percentage = 0.1,
        low_foreground = dracula['red']),
    widget.NvidiaSensors(
        background = dracula['bg'],
        foreground = dracula['green'],
        fontsize = 14,
        threshold = 80,
        foreground_alert = dracula['red'],
        update_interval = 2,),
    #widget.ThermalSensor(
    #    background = dracula['bg'],
    #    foreground = dracula['pink'],
    #    tag_sensor = 'k10temp-pci-00c3',
    #    #format = '{CPU}: {temp: .1f}',
    #    threshold = 60.0,
    #    foregrount_alert = dracula['red'],
    #    update_interval = 2),
    widget.ThermalZone(
        background= dracula['bg'],
        fgcolor_normal = dracula['pink'],
        fgcolor_crit = dracula['red'],
        fgcolor_high = dracula['magenta'],
        zone = '/sys/class/thermal/thermal_zone0/temp',
        update_interval = 2.0,
        high = 75,
        crit = 90,
        format_crit = '{temp}°C CRIT!'
    ),
    widget.CurrentLayout(
        fontsize = 14,
        foreground = dracula['yellow'],
        background = dracula['bg'],
        padding =5),
    #widget.TextBox(
    #    fontaize = 14,
    #    text="",
    #    padding = 6,
    #    foreground = dracula['green'],
    #    background = dracula['bg']),
    #widget.Volume(
    #    fontsize = 14,
    #    foreground = dracula['green'],
    #    background = dracula['bg'],
    #    volume_app = 'pamixer',
    #    volume_down_command = 'pamixer --decrease 5',
    #    volume_up_command = 'pamixer --increase 5',
    #),

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
    #widget.TextBox(
    #    fontaize = 14,
    #    text="",
    #    padding = 6,
    #    foreground = dracula['green'],
    #    background = dracula['bg']),
    #widget.Volume(
    #    fontsize = 14,
    #    foreground = dracula['green'],
    #    background = dracula['bg'],),
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
    #widget.Systray(
    #    background = dracula['bg'],
    #    padding = 5),
    
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

