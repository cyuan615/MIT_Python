# Debugging example:
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = input('Enter an element: ')
        result.append(elem)
    if isPal(result):
        print('yes')
    else:
        print('no')

silly(5)
