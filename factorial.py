import os, argparse, sys
sys.set_int_max_str_digits(0)

# Top down recursive implementation
def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number- 1)

# Not using recursion
def factorial_loop(n):
    product = 1
    for num in range(1, n + 1):
        product *= num
    return product

# Bottom up recursive implementation
def factorial2(n, i = 1, product = 1):
    if i > n:
        return product
    return factorial2(n, i + 1, product * i)

parser = argparse.ArgumentParser(
    prog='factorial',
    description='Calculate the factorial of a number.')

parser.add_argument('startingValue', type=int,
    help='Number for which to calculate its factorial.')

parser.add_argument('-r', '--recurse', action='store_true', help='Use a recursive method.')

args = parser.parse_args()

if args.recurse:
    fac = factorial(args.startingValue)
else:
    fac = factorial_loop(args.startingValue)
print(f'{args.startingValue}! = {fac} (calculated with{"" if args.recurse else "out"} recursion)\n')
