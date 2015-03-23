if !has('python')
         finish
endif

function! Inst()
    pyfile ../../work/python/fileparse.py
endfunc

command! Inst call Inst()
