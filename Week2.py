## Week 2:
"""
# Simple Algorithms:
# 1.
s = 'aliwurfhacbdsj'
for index in range (len(s)):
    if s[index] == 'o' or s[index] == 'i':
        print('yes')
# string is iterative:
for char in s:
    if char == 'i' or char == 'o':
        print('yes')

an_letter = 'aeiou'

# 2.
word = input('Enter a word: ')
i = 0
while i != len(word):
    if word[i] in an_letter:
        print('Give me an ' + word[i])
    else:
        print('Give me a ' + word[i])
    i += 1

# Approximate Solutions:
cube = 98
e = 0.01
guess = 0
increment = 0.0001
num_guess = 0
while abs(guess**3 - cube) >= e:
    guess += increment
    num_guess += 1
print(guess)
print(num_guess)


# Bisection Search

# 1. square root
x = 25
e = 0.01
numGuess = 0
low = 4
high = 6
ans = (low + high)/2

while abs(ans**2 - x) >= e:
    numGuess += 1
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low)/2

print(ans)
print(numGuess)

#2. cube root
x = 27
e = 0.01
numGuess = 0
low = 1
hight = 27
ans = (high + low) / 2

while abs(ans**3 - x) >= e:
    numGuess += 1
    if ans**3 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2

print(ans)
print(numGuess)

# Newton Raphson:

e = 0.01
y = 87
guess = y/2.0
numGuess = 0

while abs(guess * guess - y) >= e:
    numGuess += 1
    guess = guess - (((guess ** 2) - y)/(2 * guess))
print('numGuess = ' + str(numGuess))
print('Square root of ' + str(y) + ' is about ' + str(guess))


# Function:
# 1.example:
def is_even(i):
    print('hi')
    return i % 2 == 0
print(is_even(3))

# Calling Functions and Scope
# 1.
def f_a():
    print('inside f_a')

def f_b(y):
    print('inside f_b')
    return y

def f_c(z):
    print('inside f_c')
    return z()

print(f_a())
print(5 + f_b(2))
print(f_c(f_a))

# 2.
def f(y):
    x = 1
    x += 1
    print(x)

x = 5
f(x)
print(x)

def g(y):
    print(x)
    print(x + 1)

x = 5
g(x)
print(x)

def h(y):
    x = x + 1

x = 5
h(x)
print(x)

# unboundLocalError: x referenced before assignment

# 3.
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)

# keywords arguments

def printname(fn,ln,reverse):
    if reverse:
        print(ln + ', ' + fn)
    else:
        print(fn + ', ' + ln)

printname('Cindy','Yuan', True)
printname(fn = 'Cindy',ln = 'Yuan', reverse=True)


# binding a default value to reverse
def printname(fn,ln,reverse = False):
    if reverse:
        print(ln + ', ' + fn)
    else:
        print(fn + ', ' + ln)

# Iteration and Recursion
# 1. multiply
def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a,b - 1)

# 2.factorial n! = n * (n-1) * (n-2) * ....* 1
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))


# Inductive Reasoning
# Towers of Hanoi

def printMove(fr,to):
    print('move from ' + str(fr) + ' to ' + str(to))

def towers(n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        towers(n-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(n-1,spare,to,fr)

print(towers(5,1,2,3))


# Fibonacci: multiple bases

female(0) = 1
female(1) = 1

female(n) = female(n - 1) +  female(n - 2)


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))


# non numerical
def toChars(s):
    s = s.lower()
    ans = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans = ans + c
    return ans

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])


def isPalindrome(s):
## convert string to char and lower case and remove space
    return isPal(toChars(s))

#if __name__ == '__main__':
print(isPalindrome('ifia'))

def isPal1(s):
    b = 0
    e = -1

    while b <= len(s)/2:
        if s[b] not in 'abcdefghijklmnopqrstuvwxyz':
            b += 1
            continue
        if s[e] not in 'abcdefghijklmnopqrstuvwxyz':
            e -= 1
            continue
        if s[b] == s[e]:
            b += 1
            e -= 1
        else:
            return False
            break
    return True


print(isPal1('abb ba'))
"""
# problem set 1:
# 1. Method 1: for loop
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
def balance(n):
    i = 1
    newbalance = n
    while i <= 12:

        payment = newbalance * monthlyPaymentRate
        unpaidbalance = newbalance - payment
        newbalance = unpaidbalance * (1 + annualInterestRate / 12)
        i += 1

    return newbalance

print(round(balance(42),2))

# Method 2: recursion

def balance1(n,i):

    if i == 1:
        return n
    else:
        return (0.96 * 0.2/12 + 0.96) * balance1(n,i-1)

print(balance1(42,12))

# Problem Set 2:
