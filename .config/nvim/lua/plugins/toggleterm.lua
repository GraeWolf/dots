local config = function()
    require("toggleterm").setup{
        open_mapping = [[<c-\>]],
    }
end

return {
  {'akinsho/toggleterm.nvim', version = "*",
        lazy = false,
        opts = {--[[ things you want to change go here]]},
        config = config},
}
