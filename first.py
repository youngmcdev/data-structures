import os

# Counts down to zero using a while loop. No recursion.
def countdown1(number):
    while number >= 0:
        print(number)
        number -= 1

# Counts down using recursion.
def countdown2(number):
    print(number)

    if number < 0:
        return 0
    if number == 0:
        return
    countdown2(number - 1)

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number- 1)

def print_subdir_one_level(directoryName):
    isDirectory = os.path.isdir(directoryName)
    print(f'Searching for, {directoryName}, which is {"" if isDirectory else "NOT "}a directory.')
    if not isDirectory:
        return
    
    dirList = os.listdir(directoryName)
    print(f'Found {len(dirList)} files.')
    dirCount = 0

    for filename in dirList:
        fullPath = os.path.join(directoryName, filename)
        isDirectory = os.path.isdir(fullPath)
        
        if isDirectory:
            dirCount += 1
            print(fullPath)
        # else:
            # print(f'  {filename} is not a directory.')
    print(f'  {dirCount} directories found.')


def print_subdir_two_levels(directoryName):
    isDirectory = os.path.isdir(directoryName)
    print(f'Searching for, {directoryName}, which is {"" if isDirectory else "NOT "}a directory.')
    if not isDirectory:
        return
    
    for filename in os.listdir(directoryName):
        path = os.path.join(directoryName, filename)
        if os.path.isdir(path):            
            print(path)

            for filename2 in os.listdir(path):
                path2 = os.path.join(path, filename2)
                if os.path.isdir(path2):
                    print(path2)

def print_subdir_recurse(directoryName):
    isDirectory = os.path.isdir(directoryName)
    print(f'Searching for, {directoryName}, which is {"" if isDirectory else "NOT "}a directory.')
    if not isDirectory:
        return
    
    for filename in os.listdir(directoryName):
        path = os.path.join(directoryName, filename)
        if os.path.isdir(path):
            print(path)
            print_subdir_recurse(path)

def sum(low, high):
    # Base case:
    if high <= low:
        return high

    return high + sum(low, high - 1)


def fib_simple(nthFibNumber):
    if nthFibNumber == 0 or nthFibNumber == 1:
        return nthFibNumber

    return fib_simple(nthFibNumber - 2) + fib_simple(nthFibNumber - 1)

def fib_simple_alt(nthFibNumber, countTable):
    if nthFibNumber not in countTable:
        countTable[nthFibNumber] = 1
    else:
        countTable[nthFibNumber] = countTable[nthFibNumber] + 1
    
    print(countTable)

    if nthFibNumber == 0 or nthFibNumber == 1:
        return nthFibNumber

    return fib_simple_alt(nthFibNumber - 2, countTable) + fib_simple_alt(nthFibNumber - 1, countTable)


def fib_memo(nthFibNumber, memo):
    if nthFibNumber == 0 or nthFibNumber == 1:
        return nthFibNumber

    if nthFibNumber not in memo:
        memo[nthFibNumber] = fib_memo(nthFibNumber - 2, memo) + fib_memo(nthFibNumber - 1, memo)
        print(memo)        

    return memo[nthFibNumber]


def fib_memo_alt(nthFibNumber, memo, countTable):
    if nthFibNumber not in countTable:
        countTable[nthFibNumber] = 1
    else:
        countTable[nthFibNumber] = countTable[nthFibNumber] + 1

    print(countTable)

    if nthFibNumber == 0 or nthFibNumber == 1:
        return nthFibNumber

    if nthFibNumber not in memo:
        memo[nthFibNumber] = fib_memo_alt(nthFibNumber - 2, memo, countTable) + fib_memo_alt(nthFibNumber - 1, memo, countTable)   

    return memo[nthFibNumber]


def fib_iterate(nthFibNumber):
    if nthFibNumber == 0:
        return 0

    currentFibNumber = 0
    nextFibNumber = 1

    for _ in range(1, nthFibNumber):
        currentFibNumber, nextFibNumber = nextFibNumber, currentFibNumber + nextFibNumber

    return nextFibNumber

def double_array_loop(array):
    index = 0
    while index < len(array):
        array[index] *= 2
        index += 1

def double_array(array, index = 0):
    # Base case: when the index goes past 
    # the end of the array
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)


def reverse(string):
    if not string:
        return ""
    return reverse(string[1:]) + string[0]

# Staircase Problem
def number_of_paths(n):
    # Muliple base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return (number_of_paths(n - 1)
        + number_of_paths(n - 2)
        + number_of_paths(n - 3))


#countdown1(6)
countdown2(-5)
#print(factorial(10))
#print_subdir_one_level("C:\logs")
#print_subdir_two_levels("C:\\repos")
#print_subdir_recurse("C:\\repos")
#print(sum(1, 10))
#print(fib_simple(10))
#print(fib_simple_alt(10, {}))
#print(fib_memo(10, {}))
#print(fib_memo_alt(10, {}, {}))
#print(fib_iterate(10))
