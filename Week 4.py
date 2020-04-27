'''
# Debugging example:
def isPal(x):
    assert type(x) == list
    temp = x[:]
    temp.reverse()
    print(temp,x)
    if temp == x:
        return True
    else:
        return False


def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter an element: ')
        result.append(elem)
    if isPal(result):
        print('yes')
    else:
        print('no')

silly(2)
'''

a = 'abc'
b = list(a)
print(b)