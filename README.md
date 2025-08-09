# Data Structures 2025
Trying concepts from Jay Wengrow's book.

## Recursion

### Count Down to Zero

Supply an integer, n. _n_, and each consecutive number, down to zero, will be printed to the console.

- File: count-down.py
- Display Help: `python .\count-down.py -h`

#### Examples

- `python .\count-down.py 20`
  - Counts down without recursion.
- `python .\count-down.py 20 --recurse`
  - Counts down using recursion.

### List the Subdirectories of A Given Directory 

Supply a directory on your file system. The subdirectories will be printed to the console.

- File: sub-directory.py
- Display Help: `python .\sub-directory -h`

#### Examlpes

- `python .\sub-directory.py c:\logs --level 1`
  - Goes down one level displaying only the children of the supplied directory.
  - This does _not_ use recursion.
- `python .\sub-directory.py c:\logs --level 2`
  - Displays the children of the supplied directory one and two levels down.
  - This does _not_ use recursion.
- `python .\sub-directory.py c:\logs --level 0`
  - Uses recursion to display _all_ subdirectories of the supplied directory.

### Calculate N Factorial

Supply an integer, n. _n factorial_ will be printed to the console. 

- File: factorial.py
- Display Help: `python .\factorial -h`

#### Examlpes

- `python .\factorial.py 20`
  - Uses a non-recursive algorithm.
- `python .\factorial.py --recurse 20`
  - Uses a recursive algorithm.

### Generate the Reversal of A Given String

Supply a string and the reversal of it will be printed to the console. Use double quotes if supplying more than one word.

- File: reverse.py
- Display Help: `python .\reverse -h`

#### Examlpes

- `python .\reverse.py counterintelligence`
- `python .\reverse.py "The Cat in The Hat"`
  - There's only a recursive implementation.

### Calculate the Nth Fibonacci Number

Supply an integer, n. The _nth_ Fibonacci number will be printed to the console.  

- File: fibonacci.py
- Display Help: `python .\fibonacci.py -h`

There are three variations.

1. An iterative, non-recursive method.
2. A simple, recursive method.
    - This is the default method when an algorithm is not specified.
3. An optimized, recursive method using memoization.

Along with the above variations the efficiency of the simple and optimized methods may be compared. The _ST_ and _MT_ options display a dictionary of key/value pairs where the key is the number (not the value) of the Fibonacci number being calculated and the value is the number of times, due to recursion, it was calculated. Thus, `(9, 144)` indicates the 9th Fibonacci number was calculated 144 times.  

#### Examlpes

- `python .\fibonacci.py 20 --algorithm I`
  - Uses the non-recursive method.
- `python .\fibonacci.py 20 --algorithm S`
  - Uses the simple, recursive method.
- `python .\fibonacci.py 20 --algorithm M`
  - Uses the optimized, recursive method.
- `python .\fibonacci.py 20 --algorithm ST`
  - Uses the simple, recursive method and displays a summary of how many times each Fibonacci number was calculated.
- `python .\fibonacci.py 20 --algorithm MT`
  - Uses the optimized, recursive method and displays a summary of how many times each Fibonacci number was calculated.

### Calculate the Number of Paths to the Top of A Staircase

Supply an integer, n. The number of paths to the top of a staircase have _n_ stairs will be printed to the console.

- File: calculate-paths.py
- Display Help: `python .\calculate-paths.py -h`

#### Examlpes

- `python .\calculate-paths 11`
  - There's only a recursive implementation.

## Tries

### Files

- trie_node.py: _TrieNode_ class - Nodes that make up the tree.
- trie.py: _Trie_ class - Encapsulates the tree and the operations that may be performed on it.
- trie_tests.py: Script for testing the Trie class and its operations.
  - Execute `python .\trie_tests.py -h` to display the help message.
- dictionaries\\: Each file in this directory contains a list of words which is meant to populate a Trie and allow operations to be performed.
  - a.txt: Words that begin with the letter 'a'.
  - one.txt: A small collection of words.

### Examples

The following exapmles will use `.\dictionaries\a.txt` for the list of words on which to operate. Thus they assume those words are present.

- `python .\trie_tests.py -h`
  - Displays the program's help page and its syntax.
- `python .\trie_tests.py .\dictionaries\a.txt -f list`
  - Lists all the words in the dictionary.
- `python .\trie_tests.py .\dictionaries\a.txt -f search -v ac`
  - Searches the dictionary for the _prefix_ passed for the `-v` option, 'ac'. The keys of next node will be displayed on the command line.
- `python .\trie_tests.py .\dictionaries\a.txt -f match -v ace`
  - Searches the dictionary for an _exact match_ to the value passed for the `-v` option.
- `python .\trie_tests.py .\dictionaries\a.txt -f complete -v ac`
  - Searches the dictionary for the _prefix_ passed for the `-v` option, 'ac'. All possible _suffixes_ that can complete a word will be displayed on the command line.
- The _correct_ function will attempt autocorrecting the value passed for the `-v` option. Note the difference when one letter is changed.
  - `python .\trie_tests.py .\dictionaries\a.txt -f correct -v agaip` returns "again".
  - `python .\trie_tests.py .\dictionaries\a.txt -f correct -v agatp` returns "agast".
- `python .\trie_tests.py .\dictionaries\a.txt -f bfs`
  - Displays all nodes in the trie using Breadth First Search.