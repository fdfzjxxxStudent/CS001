#list8.py
def exist(l,c):
    if c in l:
        return True
    else:
        return False

letters=['a','b','c','d','e']
if exist(letters,'a'):
    print('Found in ',end='')
    print(letters.index('a'))
else:
    print('Not found.')

