set tabstop=4
set expandtab

autocmd! InsertEnter * call libcall('libvimlib.so', 'insertenter', [])
autocmd! InsertLeave * call libcall('libvimlib.so', 'insertleave', [])
autocmd! VimLeave * call libcall('libvimlib.so', 'savedata', [])
