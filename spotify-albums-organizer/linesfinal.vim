function! Lines(query)
  let n = line(".")
  let m = search(a:query)
  let m = line(".")
  let nextOccur = m-n
  let back = m-n
  let k = ''
  if nextOccur > 1
    while back > 0
      let k = k."k"
      let back -= 1
    endwhile
    :execute "normal ".k
    :execute "normal $".nextOccur."gJ"
  endif
endfunction

:execute "normal gg"
:execute 'g/\<master id=/call Lines("<master id=")'
:execute 'wq'
