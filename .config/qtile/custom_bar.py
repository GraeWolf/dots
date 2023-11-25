from libqtile import bar, widget

from colors import kanagawa
gb_font = 18


widgets_list = [
    widget.GroupBox(
        fontsize=gb_font,
        active=kanagawa['blue'],
        inactive=kanagawa['grey'],
        highlight_method="block",
        highlight_color=kanagawa['bg'],
        this_current_screen_border=kanagawa['fg_gutter'],
        other_current_screen_border=kanagawa['orange'],
        other_screen_border=kanagawa['orange'],
        this_screen_border=kanagawa['blue'],
        foreground=kanagawa['blue'],
        background=kanagawa['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize=gb_font,
        foreground=kanagawa['orange'],
        background=kanagawa['bg'],
        padding=5),
    widget.Battery(
        background=kanagawa['bg'],
        foreground=kanagawa['magenta'],
        fontsize=gb_font,
        format='{char}{percent:2.0%}',
        low_percentage=0.1,
        low_foreground=kanagawa['red']),
    widget.NvidiaSensors(
        background=kanagawa['bg'],
        foreground=kanagawa['green'],
        fontsize=gb_font,
        threshold=80,
        foreground_alert=kanagawa['red'],
        update_interval=2,),
    # widget.ThermalSensor(
    #    background = kanagawa['bg'],
    #    foreground = kanagawa['pink'],
    #    tag_sensor = 'k10temp-pci-00c3',
    #    #format = '{CPU}: {temp: .1f}',
    #    threshold = 60.0,
    #    foregrount_alert = kanagawa['red'],
    #    update_interval = 2),
    widget.ThermalZone(
        fontsize=gb_font,
        background=kanagawa['bg'],
        fgcolor_normal=kanagawa['pink'],
        fgcolor_crit=kanagawa['red'],
        fgcolor_high=kanagawa['magenta'],
        zone='/sys/class/thermal/thermal_zone0/temp',
        update_interval=2.0,
        high=75,
        crit=90,
        format_crit='{temp}°C CRIT!'
    ),
    widget.CurrentLayout(
        fontsize=gb_font,
        foreground=kanagawa['yellow'],
        background=kanagawa['bg'],
        padding=5),
    widget.TextBox(
        fontaize=gb_font,
        text="",
        padding=6,
        foreground=kanagawa['green'],
        background=kanagawa['bg']),
    widget.Volume(
        fontsize=gb_font,
        foreground=kanagawa['green'],
        background=kanagawa['bg'],
        volume_app='pamixer',
        volume_down_command='pamixer --decrease 5',
        volume_up_command='pamixer --increase 5',
     ),

    widget.Clock(
        fontsize=gb_font,
        foreground=kanagawa['blue'],
        background=kanagawa['bg'],
        format="%A, %B %d  - "),
    widget.Clock(
        fontsize=gb_font,
        foreground=kanagawa['red'],
        background=kanagawa['bg'],
        format="%H:%M"),
    widget.Sep(
        linewidth=0,
        padding=5,
        background=kanagawa['bg'],),
    widget.LaunchBar(progs=[
        ('⏾', 'sleeplock', 'put computer to sleep')],
        fontsize=gb_font,
        foreground=kanagawa['white'],
        background=kanagawa['bg'],
        padding=5,
        # default_icon='/usr/share/icons/Adwaita/24x24/status/night-light-symbolic.symbolic.png'
         ),
    widget.Sep(
        linewidth=0,
        padding=5,
        background=kanagawa['bg'],),
    widget.Systray(
       background=kanagawa['bg'],
       padding=5),
    widget.Sep(
        linewidth=0,
        padding=5,
        background=kanagawa['bg'],),
]

bar1 = bar.Bar(widgets=widgets_list,
               margin=[10, 10, 5, 10],
               opacity=1,
               size=35
               )

bar2 = bar.Bar(widgets=widgets_list[:12],
               margin=[10, 10, 5, 10],
               opacity=1,
               size=35
               )
