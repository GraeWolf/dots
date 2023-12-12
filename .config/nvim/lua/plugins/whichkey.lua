return {
	"folke/which-key.nvim",
	keys = { "<leader>" },
	config = function()
		local which_key = require("which-key")
        vim.o.timeout = true
        vim.o.timeoutlen = 100

		which_key.setup({
			plugins = {
                registers = true,
				spelling = {
					enabled = true,
					suggestions = 20,
				},
                presets = {
                    operators = true,
                    motions = true,
                    text_objects = true,
                    windows = true,
                    nav = true,
                },
			},
            operators = { gc = "Comments" },
            motions = {
                count = true,
            },
            icons = {
                breadcrumb = ">>",
                separator = "->",
                group = "+",
            },
            ignore_missing = false,
            show_help = true,
            show_keys = true,
			window = {
				border = "shadow",
				position = "bottom",
				margin = { 0, 1, 1, 5 },
				padding = { 1, 2, 1, 2 },
			},
			triggers_nowait = {
				"`",
				"'",
				"g`",
				"g'",
				'"',
				"<c-r>",
				"z=",
			},
            disable = {
                buftypes = {},
                filetypes = {},
            },
		})

		local opts = {
			prefix = "<leader>",
		}

		local groups = {
			b = { name = "buffer" },
			s = { name = "search" },
			-- g = { name = "git" },
			r = { name = "refactor" },
			l = { name = "lsp" },
			d = { name = "debug" },
			m = { name = "macro/markdown" },
			n = { name = "notifications" },
			["<tab>"] = { name = "tabs" },
			[";"] = { name = "test" },
			["'"] = { name = "marks" },
			["/"] = { name = "search" },
			["/g"] = { name = "git" },
			["/gd"] = { name = "diff" },
			["["] = { name = "previous" },
			["]"] = { name = "next" },
		}

		which_key.register(groups, opts)
	end,
}
