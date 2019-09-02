<masters>
let first = getline(1)
if first !~ '<masters>'
    execute 'normal! gg'
    execute 'put! '
    execute 'normal! I<masters>'
endif
execute 'normal! G'
let last = line(".")
let last = getline(last)
if last !~ '</masters>'
    execute 'put '
    execute 'normal! I</masters>'
endif
execute "wq"
</masters>
