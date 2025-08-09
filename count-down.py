import os, argparse

# Counts down to zero using a while loop. No recursion.
def countdown1(number):
    while number >= 0:
        print(number)
        number -= 1

# Counts down using recursion.
def countdown2(number):
    number = abs(number)
    print(number)
    
    if number == 0:
        return
    countdown2(number - 1)

parser = argparse.ArgumentParser(
    prog='count-down',
    description='Counts down to zero.',
    epilog='')

parser.add_argument('startingValue', type=int,
    help='Number from which to count down.')

parser.add_argument('-r', '--recurse', action='store_true', help='Use a recursive method.')

args = parser.parse_args()

if args.recurse:
    countdown2(args.startingValue)
else:
    countdown1(args.startingValue)

print(f'(calculated with{"" if args.recurse else "out"} recursion)\n')