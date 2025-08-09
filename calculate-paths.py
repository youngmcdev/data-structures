import os, argparse

def number_of_paths(n):
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

parser = argparse.ArgumentParser(
    prog='number_of_paths',
    description='Calculate the number of paths to the top of a stair case.')

parser.add_argument('number_of_stairs', type=int, help='The number of stairs that make up the stair case.')

args = parser.parse_args()

numOfPaths = number_of_paths(args.number_of_stairs)
print(f'Number of possible paths to the top: {numOfPaths}\n')

