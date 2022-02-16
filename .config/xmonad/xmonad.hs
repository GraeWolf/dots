-- All the imports needed for functionality
--
import XMonad

import qualified Data.Map as M
import Data.Maybe (fromJust)
import Data.Monoid

import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.ManageDocks
import XMonad.Hooks.ManageHelpers
import XMonad.Hooks.StatusBar
import XMonad.Hooks.StatusBar.PP

import XMonad.Layout.BinarySpacePartition
import XMonad.Layout.Fullscreen
import XMonad.Layout.LayoutModifier
import XMonad.Layout.SimplestFloat
import XMonad.Layout.Spacing

import XMonad.Util.ClickableWorkspaces
import XMonad.Util.EZConfig
import XMonad.Util.Loggers
import XMonad.Util.Ungrab
import XMonad.Util.Run
import XMonad.Util.SpawnOnce

myTerminal :: String
myTerminal = "alacritty"

myBorderWidth :: Dimension
myBorderWidth = 2

myStartupHook :: X ()
myStartupHook = do
  spawn "killall trayer" -- kill current tryaer on each restart

  spawnOnce "~/bin/autostart.sh"

  spawn ("sleep 10 && trayer --edge top --align right --SetDockType true --SetPartialStrut true --expand true --widthtype request --transparent false --tint 0x3b4252 --height 32 --padding 3 --margin 3")

myXmobarPP :: PP
myXmobarPP = def
    { ppSep             = magenta " | "
    , ppTitleSanitize   = xmobarStrip
    , ppCurrent         = magenta . wrap (green "[") (green "]") 
    , ppHidden          = magenta . wrap " " ""
    , ppHiddenNoWindows = blue . wrap " " ""
    , ppUrgent          = red . wrap (yellow "!") (yellow "!")
    , ppLayout          = snowstorm1
    , ppTitle           = yellow . wrap(blue "[") (blue "]")
    , ppOrder           = \(ws:l:t:_) -> [ws, l, t]
    --, ppExtras          = [logTitles formatFocused formatUnfocused]
    --, ppExtras          = [logTitle]
    }
  where
    --formatFocused   = wrap (white    "[") (white    "]") . magenta . ppWindow
    --formatUnfocused = wrap (lowWhite "[") (lowWhite "]") . blue    . ppWindow

    -- | Windows should have *some* title, which should not not exceed a
    -- sane length.
    ppWindow :: String -> String
    ppWindow = xmobarRaw . (\w -> if null w then "untitled" else w) . shorten 30

    blue, lowWhite, magenta, red, white, yellow, green, frost1, frost2, frost3 :: String -> String
    magenta  = xmobarColor "#b48ead" ""
    blue     = xmobarColor "#5e81ac" ""
    white    = xmobarColor "#eceff4" ""
    yellow   = xmobarColor "#ebcb8b" ""
    red      = xmobarColor "#bf616a" ""
    lowWhite = xmobarColor "#e5e9f0" ""
    green    = xmobarColor "#a3be8c" ""
    frost1   = xmobarColor "#8fbcbb" ""
    frost2   = xmobarColor "#88c0d0" ""
    frost3   = xmobarColor "#81a1c1" ""
    snowstorm1 = xmobarColor "#d8dee9" ""

-- myWorkspaces = [" dev ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]
myWorkspaces = ["1:<fn=1>\61728</fn>", "2:<fn=1>\62057</fn>", "3:<fn=1>\61723</fn>", "4:<fn=1>\61515</fn>", "5:<fn=1>\61468</fn>", "6:<fn=1>\62744</fn>", "7:<fn=1>\61557</fn>", "8:<fn=1>\61729</fn>", "9:<fn=1>\61441</fn>"]
--myWorkspaceIndices = M.fromList $ zipWith (,) myWorkspaces [1..] -- (,) == \x y -> (x,y)

myNormalBorderColor = "#5e81ac"
myFocusedBorderColor = "#bf616a"

myManageHook :: XMonad.Query (Data.Monoid.Endo WindowSet)
myManageHook = composeAll
    -- 'doFloat' forces a window to float.  Useful for dialog boxes and such.
    -- using 'doShift ( myWorkspaces !! 7)' sends program to workspace 8!
    -- I'm doing it this way because otherwise I would have to write out the full
    -- name of my workspaces and the names would be very long if using clickable workspaces.
    [ className =? "confirm"         --> doFloat
    , className =? "file_progress"   --> doFloat
    , className =? "dialog"          --> doFloat
    , className =? "download"        --> doFloat
    , className =? "error"           --> doFloat
    , className =? "notification"    --> doFloat
    , className =? "splash"          --> doFloat
    , className =? "toolbar"         --> doFloat
    , className =? "Yad"             --> doCenterFloat
    , title =? "Oracle VM VirtualBox Manager"  --> doFloat
    , title =? "Mozilla Firefox"     --> doShift ( myWorkspaces !! 1 )
    , className =? "Vivaldi-stable"   --> doShift ( myWorkspaces !! 1 )
    , className =? "mpv"             --> doShift ( myWorkspaces !! 7 )
    , className =? "VirtualBox Manager" --> doShift  ( myWorkspaces !! 4 )
    , (className =? "firefox" <&&> resource =? "Dialog") --> doFloat  -- Float Firefox Dialog
    , isFullscreen -->  doFullFloat
    ]


myConfig = def
    { modMask = mod4Mask    --Rebind Mod to the Super key
    , layoutHook = myLayout --Use custom layouts
    , workspaces = myWorkspaces
    , manageHook = myManageHook
    , startupHook = myStartupHook
    , borderWidth = myBorderWidth
    , normalBorderColor = myNormalBorderColor
    , focusedBorderColor = myFocusedBorderColor
    }
  `additionalKeysP`
    [-- Xmonad keys
      ("M-C-r", spawn "xmonad --recompile") 
     ,("M-S-r", spawn "xmonad --restart")
     ,("M-q", kill)
     -- Useful Programs
     ,("M-]"       , spawn "vivaldi-stable" )
     ,("M-<Return>", spawn (myTerminal))
     ,("M-d"       , spawn "rofi -modi drun -show drun")
     ,("M-S-<Return>", spawn "thunar")
     -- Volume
     ,("<XF86AudioLowerVolume>", spawn "pactl set-sink-volume @DEFAULT_SINK@ -5%")
     ,("<XF86AudioRaiseVolume>", spawn "pactl set-sink-volume @DEFAULT_SINK@ +5%")
     ,("<XF86AudioMute>", spawn "pactl set-sink-mute @DEFAULT_SINK@ toggle" )
    ]

myLayout = smartSpacing 4
  $fullscreenFull
  $avoidStruts(tiled ||| Mirror tiled ||| Full ||| emptyBSP ||| simplestFloat)
  where
    tiled = Tall nmaster delta ratio
    nmaster = 1     -- Default number of windows in the master pane
    ratio   = 1/2   -- Default proportion of screen occupied by master pane
    delta   = 3/100 -- Percent of screen to increment by when resizing panes


main :: IO ()
main = xmonad
     . ewmhFullscreen
     . ewmh
     . withEasySB (statusBarProp "xmobar" (clickablePP myXmobarPP)) defToggleStrutsKey
     $ myConfig
