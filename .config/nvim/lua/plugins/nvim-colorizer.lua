return {
    "NvChad/nvim-colorizer.lua",
    lazy = false,
    opts = {
      user_default_options = {
        mode = "virtualtext", -- You can change the mode to "foreground" to colorize foreground color codes
        RGB = true, -- Enable RGB color notation support
        RRGGBB = true, -- Enable RRGGBB color notation support
        names = false, -- Disable color name highlighting (e.g., "red", "blue", etc.)
        css = false, -- Disable CSS color notation support      
      }
    }
}
