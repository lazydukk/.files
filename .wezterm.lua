-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices
config.default_prog = { 'pwsh.exe' }
config.font = wezterm.font 'ZedMono Nerd Font'
font_size = 12.0
line_height = 1

window_frame = {
 font = wezterm.font { family = 'Inter', weight = 'Regular' },
}


--

-- For example, changing the color scheme:
config.color_scheme = 'Catppuccin Mocha'

-- and finally, return the configuration to wezterm
return config