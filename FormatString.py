text = 'Hello World'
text.ljust(20)
text.rjust(20)
text.center(20)
text.rjust(20,'=')
text.center(20,'*')
format(text, '>20')
format(text, '<20')
format(text, '^20')
format(text, '*^20s')

'{:>10s} {:>10s}'.format('Hello', 'World')