import os, argparse

# Non-recursive algorithm
def fib_iterate(nthFibNumber):
    if nthFibNumber == 0:
        return 0

    currentFibNumber = 0
    nextFibNumber = 1

    for _ in range(1, nthFibNumber):
        currentFibNumber, nextFibNumber = nextFibNumber, currentFibNumber + nextFibNumber

    return nextFibNumber


def fib_simple(nthFibNumber):
    if nthFibNumber == 0 or nthFibNumber == 1:
        return nthFibNumber

    return fib_simple(nthFibNumber - 2) + fib_simple(nthFibNumber - 1)

def fib_simple_table(nthFibNumber, countTable):
    if nthFibNumber not in countTable:
        countTable[nthFibNumber] = 1
    else:
        countTable[nthFibNumber] = countTable[nthFibNumber] + 1
    
    if nthFibNumber == 0 or nthFibNumber == 1:
        return nthFibNumber

    return fib_simple_table(nthFibNumber - 2, countTable) + fib_simple_table(nthFibNumber - 1, countTable)


def fib_memoization(nthFibNumber, memo):
    if nthFibNumber == 0 or nthFibNumber == 1:
        return nthFibNumber

    if nthFibNumber not in memo:
        memo[nthFibNumber] = fib_memoization(nthFibNumber - 2, memo) + fib_memoization(nthFibNumber - 1, memo)

    return memo[nthFibNumber]


def fib_memoization_table(nthFibNumber, memo, countTable):
    if nthFibNumber not in countTable:
        countTable[nthFibNumber] = 1
    else:
        countTable[nthFibNumber] = countTable[nthFibNumber] + 1

    if nthFibNumber == 0 or nthFibNumber == 1:
        return nthFibNumber

    if nthFibNumber not in memo:
        memo[nthFibNumber] = fib_memoization_table(nthFibNumber - 2, memo, countTable) + fib_memoization_table(nthFibNumber - 1, memo, countTable)   

    return memo[nthFibNumber]


parser = argparse.ArgumentParser(
    prog='fibonacci',
    description='Calculates the Nth number in the fibonacci sequence.',
    epilog='')

parser.add_argument('nthFibonacciNumber', type=int,
    help='Which number in the sequence would you like?')

parser.add_argument('-a', '--algorithm', type=str, choices=['I','S', 'M', 'ST', 'MT'], default='S', 
    help='Select an algorithm to be used when calculating the Nth Fibonacci number. "I": Iterative, non-recursive. "S": Simple recursive. "M": Recursive using memoization, "ST", "MT"')
#parser.add_argument('-r', '--recurse', action='store_true', help='Use a recursive method.')

args = parser.parse_args()
usingRecursion = True
nthNum = args.nthFibonacciNumber

memoTable = {}
countTable = {}
match args.algorithm:
    case 'I':
        fib = fib_iterate(nthNum)
        usingRecursion = False
    case 'M':
        fib = fib_memoization(nthNum, memoTable)
    case 'ST':
        fib = fib_simple_table(nthNum, countTable)
    case 'MT':
        fib = fib_memoization_table(nthNum, memoTable, countTable)
    case _:
        fib = fib_simple(nthNum)

if len(countTable) > 0:
    sortedTable = sorted(countTable.items())
    maxKey = max(countTable, key=countTable.get)
    print(f"\nThis table displays the number of times each Fibonacci number was calculated due to recursive calls. ")
    print(f"For example the #{maxKey} Fibonacci number was calculated {countTable[maxKey]} time(s).")
    print(sortedTable)
    print("")
    
print(f'The #{nthNum} Fibonacci number is: {fib}\n(Calculated with{"" if usingRecursion else "out"} recursion)\n')