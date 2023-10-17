from libqtile import bar, widget

from colors import dracula
gb_font = 18

bar1 = bar.Bar([
    widget.GroupBox(
        fontsize = gb_font,
        active = dracula['pink'],
        inactive = dracula['grey'],
        highlight_method = "line",
        highlight_color = dracula['bg'],
        this_current_screen_border = dracula['green'],
        other_current_screen_border = dracula['orange'],
        other_screen_border = dracula['orange'],
        this_screen_border = dracula['blue'],
        foreground = dracula['blue'],
        background = dracula['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize = gb_font,
        foreground = dracula['orange'],
        background = dracula['bg'],
        padding = 5),
    widget.Battery(
        background = dracula['bg'],
        foreground = dracula['magenta'],
        fontsize = gb_font,
        format = '{char}{percent:2.0%}',
        low_percentage = 0.1,
        low_foreground = dracula['red']),
    widget.NvidiaSensors(
        background = dracula['bg'],
        foreground = dracula['green'],
        fontsize = gb_font,
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
        fontsize = gb_font,
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
        fontsize = gb_font,
        foreground = dracula['yellow'],
        background = dracula['bg'],
        padding =5),
    #widget.TextBox(
    #    fontaize = gb_font,
    #    text="",
    #    padding = 6,
    #    foreground = dracula['green'],
    #    background = dracula['bg']),
    #widget.Volume(
    #    fontsize = gb_font,
    #    foreground = dracula['green'],
    #    background = dracula['bg'],
    #    volume_app = 'pamixer',
    #    volume_down_command = 'pamixer --decrease 5',
    #    volume_up_command = 'pamixer --increase 5',
    #),

    widget.Clock(
        fontsize = gb_font,
        foreground = dracula['blue'],
        background = dracula['bg'],
        format="%A, %B %d  - "),
    widget.Clock(
        fontsize = gb_font,
        foreground = dracula['red'],
        background = dracula['bg'],
        format="%H:%M"),
    widget.LaunchBar(progs=[
        ('⏾', 'sleeplock', 'put computer to sleep')],
        fontsize = gb_font,
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
    widget.Sep(
        linewidth = 0,
        padding = 5,
        background = dracula['bg'],),

    ],

    margin=[10, 10, 5, 10],
    opacity = 0.8,
    size = 35
)

bar2 = bar.Bar([
    widget.GroupBox(
        fontsize = gb_font,
        active = dracula['pink'],
        inactive = dracula['grey'],
        highlight_method = "line",
        highlight_color = dracula['bg'],
        this_current_screen_border = dracula['green'],
        other_current_screen_border = dracula['orange'],
        other_screen_border = dracula['orange'],
        this_screen_border = dracula['blue'],
        foreground = dracula['blue'],
        background = dracula['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize = gb_font,
        foreground = dracula['orange'],
        background = dracula['bg'],
        padding = 5),
    widget.CurrentLayout(
        fontsize = gb_font,
        foreground = dracula['yellow'],
        background = dracula['bg'],
        padding =5),
    #widget.TextBox(
    #    fontaize = gb_font,
    #    text="",
    #    padding = 6,
    #    foreground = dracula['green'],
    #    background = dracula['bg']),
    #widget.Volume(
    #    fontsize = gb_font,
    #    foreground = dracula['green'],
    #    background = dracula['bg'],),
    widget.Clock(
        fontsize = gb_font,
        foreground = dracula['blue'],
        background = dracula['bg'],
        format="%A, %B %d  - "),
    widget.Clock(
        fontsize = gb_font,
        foreground = dracula['red'],
        background = dracula['bg'],
        format="%H:%M"),
    widget.LaunchBar(progs=[
        ('⏾', 'sleeplock', 'put computer to sleep')],
        fontsize = gb_font,
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
    size = 35
)

bar3 = bar.Bar([
    widget.GroupBox(
        fontsize = gb_font,
        active = dracula['pink'],
        inactive = dracula['grey'],
        highlight_method = "border",
        this_current_screen_border = dracula['green'],
        this_screen_border = dracula['blue'],
        foreground = dracula['blue'],
        background = dracula['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize = gb_font,
        foreground = dracula['orange'],
        background = dracula['bg'],
        padding = 5),
    widget.CurrentLayout(
        fontsize = gb_font,
        foreground = dracula['yellow'],
        background = dracula['bg'],
        padding =5),
    widget.Clock(
        fontsize = gb_font,
        foreground = dracula['red'],
        background = dracula['bg'],
        format="%H:%M"),
    
    ],

    margin=[10, 10, 5, 10],
    opacity = 1,
    size = 25
)

