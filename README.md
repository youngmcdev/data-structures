# Data Structures 2025
Trying concepts from Jay Wengrow's book.

## Recursion

## Tries

### Files

- trie_node.py: _TrieNode_ class - Nodes that make up the tree.
- trie.py: _Trie_ class - Encapsulates the tree and the operations that may be performed on it.
- trie_tests.py: Trying out the Trie class and its operations.
  - Execute `python .\trie_tests.py -h` to display the help message.
- ./dictionaries: Each file in this directory contains a list of words which is meant to feed a Trie and allow operations to be performed.
  - a.txt: Words that begin with the letter 'a'.
  - one.txt: A collection of words that seemed interesting.

### Examples

The following exapmles will use `.\dictionaries\a.txt` for the list of words on which to operate. Thus they assume those words are present.
- ` python .\trie_tests.py .\dictionaries\a.txt -f list`
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