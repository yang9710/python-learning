import sys

class safesub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 23
s = sub('Hello {name}, you have {n} messages.')
e = sub('Your favorite color is {color}')
print(e)