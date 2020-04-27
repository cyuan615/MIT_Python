# Week 3
###############
# Tuples:
###############
# 1.
"""
t = (2, 3, 4)
t1 = t + (5, 6)
print(t1)
print(t1[0:3])


def quotient_and_remainder(x,y):
    q = x//y
    r = x % y
    return (q,r)

(a,b) = quotient_and_remainder(16,3)
print(a,b)

# aTuple((ints,strings),(ints,strings),(),())
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)

    min_nums = min(nums)
    max_nums = max(nums)
    uniqe_words = len(words)
    return (min_nums,max_nums,uniqe_words)

print(get_data((1,'a'),(2,'h'),(3,'k')))

#########################
# Lists:
#########################
# iterate over a list
# compute the sum of elements of a list;  common patter
total = 0
for i in range(len(L)):
    total += L[i]
print(total)

total = 0
for i in L:
    total += L[i]
print(total)

# List Operations:
# 1. add more elements to end of list
l = [2,1,3]
l.append(5)
print(l)

#################################
# Mutation, Aliasing, Cloning
#################################

# Aliases:

warm = ['red','yellow','orange']
hot = warm
hot.append('pink')
# changing one changes the other!
# append has a side effect

cool = ['blue', 'green']
chill = ['blue', 'green']
chill[1] = 'grey'
print(cool)
print(chill)

# Cloning a list:
cool = ['blue', 'green']
chill = cool[:]
print(cool)
print(chill)

chill.append('grey')
print(cool)
print(chill)

# Sorting lists
# mutation and iteration
# wrong code: mutate the list
def remove_dups(l1,l2):
    for e in l1:
        if e in l2:
            l1.remove(e)

l1 = [1,2,3,4]
l2 = [1,2,5,6]
remove_dups(l1,l2)
print(l1)
# correct function:
def remove_dups1(l1,l2):
    l1_copy = l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)

l1 = [1,2,3,4]
l2 = [1,2,5,6]
remove_dups1(l1,l2)
print(l1)

# Functions as objects, dictionaries
#####################################
########### Dictionary ##############
#####################################
grades = {'Ana':'B', 'Denise':'A','John':'A+','Katy':'A'}
print(grades['John'])
# add sylvan to the dictionary
grades['Sylvan'] = 'A'
print(grades['Sylvan'])
# delete elements in the dictionary
del(grades['Ana'])
print(grades)

#####################################
# Example with Dictionaries
#####################################
# 1) create a frequency dictionary mapping str:int
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

# 2) find word that occurs the most and how many times
def most_common_words(freqs):
    value = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return(words,best)

# 3) find the words that occur at lest X times
def words_often(freqs,minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w]) # mutate the dictionary
        else:
            done = True
    return result

###########################################
# Fibonacci Recursive Code ################
###########################################

def fib(n): #fib(n) = fib(n-1) + fib(n-2),
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2) # recalculation


# more effecient method to calculate fibonacci
def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n] = ans # mutate dictionary # memorization
        return ans

d = {1:1,2:2}
print(fib_efficient(6,d))
"""
###########################################
# Global Variables ####### ################
###########################################
def fib(n): #fib(n) = fib(n-1) + fib(n-2),
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2) # recalculation


def fib_efficient(n,d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n] = ans # mutate dictionary # memorization
        return ans

numFibCalls = 0
fibArg = 12

print(fib(fibArg))
print('function call', numFibCalls)

numFibCalls = 0
d = {1:1,2:2}
print(fib_efficient(fibArg,d))
print('function call', numFibCalls)


# problem set
