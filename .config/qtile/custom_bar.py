from libqtile import bar, widget

from colors import catppuccin
gb_font = 18


widgets_list = [
    widget.GroupBox(
        fontsize=gb_font,
        active=catppuccin['blue'],
        inactive=catppuccin['grey'],
        highlight_method="block",
        highlight_color=catppuccin['bg'],
        this_current_screen_border=catppuccin['fg_gutter'],
        other_current_screen_border=catppuccin['orange'],
        other_screen_border=catppuccin['orange'],
        this_screen_border=catppuccin['blue'],
        foreground=catppuccin['blue'],
        background=catppuccin['bg']),
    widget.Prompt(),
    widget.WindowName(
        fontsize=gb_font,
        foreground=catppuccin['orange'],
        background=catppuccin['bg'],
        padding=5),
    widget.Battery(
        background=catppuccin['bg'],
        foreground=catppuccin['magenta'],
        fontsize=gb_font,
        format='{char}{percent:2.0%}',
        low_percentage=0.1,
        low_foreground=catppuccin['red']),
    widget.NvidiaSensors(
        background=catppuccin['bg'],
        foreground=catppuccin['green'],
        fontsize=gb_font,
        threshold=80,
        foreground_alert=catppuccin['red'],
        update_interval=2,),
    # widget.ThermalSensor(
    #    background = catppuccin['bg'],
    #    foreground = catppuccin['pink'],
    #    tag_sensor = 'k10temp-pci-00c3',
    #    #format = '{CPU}: {temp: .1f}',
    #    threshold = 60.0,
    #    foregrount_alert = catppuccin['red'],
    #    update_interval = 2),
    widget.ThermalZone(
        fontsize=gb_font,
        background=catppuccin['bg'],
        fgcolor_normal=catppuccin['pink'],
        fgcolor_crit=catppuccin['red'],
        fgcolor_high=catppuccin['magenta'],
        zone='/sys/class/thermal/thermal_zone0/temp',
        update_interval=2.0,
        high=75,
        crit=90,
        format_crit='{temp}°C CRIT!'
    ),
    widget.CurrentLayout(
        fontsize=gb_font,
        foreground=catppuccin['yellow'],
        background=catppuccin['bg'],
        padding=5),
    widget.TextBox(
        fontaize=gb_font,
        text="",
        padding=6,
        foreground=catppuccin['green'],
        background=catppuccin['bg']),
    widget.Volume(
        fontsize=gb_font,
        foreground=catppuccin['green'],
        background=catppuccin['bg'],
        volume_app='pamixer',
        volume_down_command='pamixer --decrease 5',
        volume_up_command='pamixer --increase 5',
     ),

    widget.Clock(
        fontsize=gb_font,
        foreground=catppuccin['blue'],
        background=catppuccin['bg'],
        format="%A, %B %d  - "),
    widget.Clock(
        fontsize=gb_font,
        foreground=catppuccin['red'],
        background=catppuccin['bg'],
        format="%H:%M"),
    widget.Sep(
        linewidth=0,
        padding=5,
        background=catppuccin['bg'],),
    widget.LaunchBar(progs=[
        ('⏾', 'sleeplock', 'put computer to sleep')],
        fontsize=gb_font,
        foreground=catppuccin['white'],
        background=catppuccin['bg'],
        padding=5,
        # default_icon='/usr/share/icons/Adwaita/24x24/status/night-light-symbolic.symbolic.png'
         ),
    widget.Sep(
        linewidth=0,
        padding=5,
        background=catppuccin['bg'],),
    widget.Systray(
       background=catppuccin['bg'],
       padding=5),
    widget.Sep(
        linewidth=0,
        padding=5,
        background=catppuccin['bg'],),
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
