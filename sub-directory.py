import os, argparse

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

parser = argparse.ArgumentParser(
    prog='sub-directory',
    description='Display the subdirectories of a directory.')

parser.add_argument('rootDirectory',
    help='The directory from which to start.')

parser.add_argument('-l', '--levels', type=int, choices=[0,1,2], default=1, help='How many levels down should we go? One (1), Two (2), or All (0)')

args = parser.parse_args()

if args.levels == 0:
    print_subdir_recurse(args.rootDirectory)
elif args.levels == 2:
    print_subdir_two_levels(args.rootDirectory)
else:
    print_subdir_one_level(args.rootDirectory)