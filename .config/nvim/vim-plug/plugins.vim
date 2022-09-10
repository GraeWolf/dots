" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')


    " Make your Vim/Neovim as smart as VSCode
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Fzf is a general-purpose command-line fuzzy finder
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
    " Python code formatter
    Plug 'ambv/black'
    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'scrooloose/NERDTree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " Nord Theme
    Plug 'arcticicestudio/nord-vim'
    " Colorizer Plugin
    Plug 'norcalli/nvim-colorizer.lua'
    " Dracula Theme
    Plug 'dracula/vim',{'name':'dracula'}

call plug#end()
