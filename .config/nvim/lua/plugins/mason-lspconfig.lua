local opts = {
    ensure_installed = {
        "efm",
        "lua_ls",
        "bashls",
        "pyright",
        "jsonls",
    },
    automatic_installation = true,
}

return {
    "Williamboman/mason-lspconfig.nvim",
    opts = opts,
    event = "BufReadPre",
    dependencies = "Williamboman/mason.nvim",
}
