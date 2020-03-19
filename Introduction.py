#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:13:02 2020

@author: yuanxinyi
"""

## Example 1

x = int(input('enter an integer: '))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')

## Example 2 compound booleans

x = 5
y = 7
z = 8

if x < y and x < z:
    print('x is the least')
elif y < z:
    print('y is the least')
else:
    print('z is the least')


## String
x = 3
ans = 0
intersleft = x
while (intersleft != 0):
    ans += x
    intersleft -= 1
print(str(x) + '*' + str(x) + '=' + str(ans))

name = 'cindy'
print(3*name)

## input/output
x = 1
print(x)
x_str = str(x)
print('my favo number is',x,'.','x =',x)


## control flow

# while loop
n = 0
while n < 5:
    print(n)
    n += 1
    
# for loop:
for n in range(5):
    print(n)

mysum = 0
for i in range(7,10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5,11,2):
    mysum += i
print(mysum)

## break:
mysum = 0
for i in range (5,11):
    mysum += i
    if mysum == 5:
        break

## interation:
x = 3
ans = 0
iter = x
while x != 0:
    ans += x
    iter = iter - 1
print(ans)

## guessing and checking
### find cube root for a number
#### only positive number

x = int(input('Enter an integer: '))
ans = 0
while ans**3 <x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print(str(x) + ' is a perfect cube')


#### consider negative number as well:

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans += 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
        print(str(x) + ' is not a perfect cube')

## problem 1:

### Method 1:
s = input('Enter your string: ')
vowels = ['a','e','i','o','u']
ans = 0
i = 0
while i != len(s):
    if s[i] in vowels:
        ans += 1
    i += 1
print(ans)

### Method 2: why not correct?
s = input('Enter your string: ')
vowels = ['a','e','i','o','u']
ans = 0
for i in range(len(s)):
    if s[i] in vowels:
        ans += 1

print(ans)

## problem 2:
### Method 1:
s = input('Enter your string: ')
ans = 0
index = 0
while index != len(s):
    if s[index:index+3] == 'bob':
        ans += 1
    index += 1
print(ans)

### Method 2:
s = input('Enter your string: ')
ans = 0

for index in range(len(s) - 2):
    if s[index:index+3] == 'bob':
        ans += 1
print(ans)
































