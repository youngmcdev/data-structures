import os, argparse

def reverse(string):
    if not string:
        return ""
    return reverse(string[1:]) + string[0]


parser = argparse.ArgumentParser(
    prog='reverse',
    description='Generate the reversal of the string passed in.')

parser.add_argument('original_string', help='The string that will be reversed.')

args = parser.parse_args()

reverseStr = reverse(args.original_string)
print(f'Your sting reversed: {reverseStr}\n')