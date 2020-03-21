## Week 2:

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






