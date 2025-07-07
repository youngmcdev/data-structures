import os, argparse

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number- 1)

# Start with one and build up.
def factorial_loop(n):
    product = 1
    for num in range(1, n + 1):
        product *= num
    return product

# Recursive implementation
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

fac = factorial(args.startingValue)
print(f'{args.startingValue}! = {fac}')
