'''
#######################
# Debugging example:
#######################
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

a = 'abc'
b = list(a)
print(b)

########################
#  Exceptions:
########################

try:
    a = int(input('tell me one number: '))
    b = int(input('tell me another number: '))
    print(a/b)
    print('okay')
except:
    print('Bug in user input')
print('outside')

# have separate except clauses to deal with a particular type pf exception
try:
    a = int(input('tell me one number: '))
    b = int(input('tell me another number: '))
    print(a / b)
    print(a + b)
except ValueError:
    print('could not convert to a number')
except ZeroDivisionError:
    print('cannot divide by zero')
except:
    print('something went wrong')


###############################
# Example Exception Usage
###############################
# 1.
while True:                                      ## what's true?
    try:
        n = input('please enter an integer: ')
        n = int(n)
        break
    except ValueError:
        print('Input not an integer; try again')
print('correct input of an integer!')

# 2. Control Input:
data = []
file_name = input('provide a name of a file of data ')
try:
    fh = open(file_name,'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append((addIt))
finally:
    fh.close()

# 2.extension

data = []
file_name = input('provide a name of a file of data ')
try:
    fh = open(file_name,'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append((addIt))
finally:
    fh.close()

gradeData = []
if data:
    for student in data:
        try:
            gradeData.append([student[0:2],student[2]])
        except IndexError:
            gradeData.append([student[0:2],[]])


########################################
# Exceptions as Control Flow ###########
########################################
def get_ratios(L1,L2):

# Assumes: L1 and l2 are lists of equal length of numbers
# Returns: a list containing L1[i] / L2[i]

    ratios = []

    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) # NaN: not a number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

L1 = [1,2,3,4]
L2 = [5,6,7,8]
L3 = [5,6,7]
L4 = [5,6,7,0]
print(get_ratios(L1,L4))

# Example 2

test_grades = [[['peter','parker'],[80.0,70.0,85.0]],[['bruce','wayne'],[100.0,80.0,74.0]]]
test_grades1 = [[['peter','parker'],[80.0,70.0,85.0]],[['bruce','wayne'],[100.0,80.0,74.0]],[['deadpoll'],[]]]
# result = [[['peter','parker'],[80.0,70.0,85.0],78.33333],[['bruce','wayne'],[100.0,80.0,74.0],84.66667]]

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0],elt[1],avg(elt[1])])
    return new_stats

def avg(grades):
    return sum(grades)/len(grades) # len(grades) could not be 0

print(get_stats(test_grades))

# Update to:
def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0],elt[1],avgnew(elt[1])])
    return new_stats

def avgnew(grades):
    try:
        return sum(grades)/len(grades) # len(grades) could not be 0
    except ZeroDivisionError:
        print('no grades data')
        return 0.0

test_grades1 = [[['peter','parker'],[80.0,70.0,85.0]],[['bruce','wayne'],[100.0,80.0,74.0]],[['deadpoll'],[]]]
print(get_stats(test_grades1))


'''
#########################
# Assertions:
#########################
def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)

grades = [12,43,54]
print(avg(grades))


