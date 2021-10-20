# GTK theme installed with lxappearance, saved under ~/.themes/
# https://github.com/EliverLara/Nordic

# Alacritty terminal
# https://github.com/alacritty/alacritty
# https://github.com/alacritty/alacritty/wiki/Color-schemes

import os, subprocess
from libqtile import hook
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy

# Control keys on tofu
# you can see which modifiers, which are enclosed in a list, map to which keys on your system by running the xmodmap command
# 1 = mod4
# 2 = mod1
# 3 = control

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "mod1"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "mod1"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "mod1"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "mod1"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "mod1"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.spawn("rofi -show drun")),
    Key([mod], "c", lazy.spawn("kitty vi ~/test")),
]


groups = [
    Group("Teams"),
    Group("Web"),
    Group("R"),
    Group("Terminals"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
    Group("10"),
]


# Allow MODKEY+[0 through 9] to bind to groups, see
# https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder

dgroups_key_binder = simple_key_binder(mod)


#   groups = [Group(i) for i in "123456789"]
#
#   for i in groups:
#       keys.extend(
#           [
#               # mod1 + letter of group = switch to group
#   groups = [Group(i) for i in "123456789"]
#
#   for i in groups:
#       keys.extend(
#           [
#               # mod1 + letter of group = switch to group
#               Key(
#                   [mod],
#                   i.name,
#                   lazy.group[i.name].toscreen(),
#                   desc="Switch to group {}".format(i.name),
#               ),
#               # mod1 + shift + letter of group = switch to & move focused window to group
#               Key(
#                   [mod, "shift"],
#                   i.name,
#                   lazy.window.togroup(i.name, switch_group=False),
#                   desc="Switch to & move focused window to group {}".format(i.name),
#               ),
#               # Or, use below if you prefer not to switch to that group.
#               # # mod1 + shift + letter of group = move focused window to group
#               # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#               #     desc="move focused window to group {}".format(i.name)),
#           ]
#       )
MARGIN = 10

layouts = [
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2, margin=MARGIN
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(ratio=0.7, margin=MARGIN),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            20,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
            ],
            20,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False


@hook.subscribe.startup_once
def autostart():
    processes = [
        ["feh", "--bg-scale", "/home/danr/Pictures/dnord4k_dark.png"],
        ["xrandr", "--output", "DP-2", "--mode", "1920x1080", "--right-of", "DP-3"],
        ["synergy"],
    ]


# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
