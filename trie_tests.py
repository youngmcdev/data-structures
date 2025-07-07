import trie, os, argparse

# Setup arguments.
parser = argparse.ArgumentParser(
    prog='test_trie',
    description='Test our Trie methods.')

parser.add_argument('dictionaryFile',
    help='Text file containing the words to be inserted into the Trie.')

parser.add_argument('-f', '--function', type=str, choices=['search','complete', 'match', 'list', 'correct', 'bfs'], default='bfs', help='Select a function to test: "search", "complete", "match", "list", "correct", or "bfs"')
parser.add_argument('-v', '--value', type=str, default='', help='The value to use for the specified function.')
args = parser.parse_args()

print(f"[INF] Function: '{args.function}'; Value: '{args.value}'; Dictionary: '{args.dictionaryFile}'\n")

# Initialize Trie
t = trie.Trie()

# Read specified dictionary and insert the words.

if not os.path.exists(args.dictionaryFile):
    print(f"[ERR] Could not open file, {args.dictionaryFile}.\n")
    quit()

with open(args.dictionaryFile) as dictionaryFile:
    for line in dictionaryFile:
        t.insert(line.strip())




# Excute a test.

def assert_equal(x, y):
    #print(x)
    #print(y)
    if x == y:
        print("    Yes, a match was found!")
    else:
        print("    No, try again.")

if args.function == 'list':
    print(f"Here are all the words!")
    words = t.collect_all_words([])
    print(words)
    quit()
if args.function == 'bfs':
    print(f"Displaying all the nodes.")
    t.traverse_bfs()
    quit()

if args.function == 'search' and args.value:
    print(f"Searching for the prefix, '{args.value}'.")
    searchResult = t.search(args.value)
    if searchResult:
        print(searchResult.children.keys()) 
    else: print("    Nothing was found.")
    quit()

if args.function == 'complete' and args.value:
    print(f"Executing autocomplete for '{args.value}'.")
    autocompleteResults = t.autocomplete(args.value)
    if autocompleteResults:
        print(autocompleteResults)
    else: print("    Nothing was found.")
    quit()

if args.function == 'match' and args.value:
    print(f"Is there a match for '{args.value}'?")
    words = t.collect_all_words([])
    assert_equal(args.value in words, True)
    quit()

if args.function == 'correct' and args.value:
    print(f"Executing autocorrect for '{args.value}'.")
    autocorrectResults = t.autocorrect(args.value)
    if autocorrectResults:
        print(autocorrectResults)
    else: print("    Nothing was found.")
    quit()

#print(t.search('h').children.keys())
#t.traverse_bfs()
#assert_equal(t.search("h").children.keys(), {'y', 'e', 'i', 'o', 'u', 'a'})
#assert_equal(t.search('himn'), None)
#words = t.collect_all_words([])
#assert_equal('hittite' in words, True)
#assert_equal('hit' in words, True)
#assert_equal('hym' in words, False)
#suggestions = t.autocomplete('h')
#assert_equal('ittite' in suggestions, True)
#assert_equal('it' in suggestions, True)
#assert_equal('ym' in suggestions, False)
#assert_equal(t.autocorrect('hyn'), 'hymn')
#print(words)
