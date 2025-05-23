import trie

t = trie.Trie()
t.insert('hand')
t.insert('handle')
t.insert('ham')
t.insert('hall')
t.insert('hat')
t.insert('hand')
t.insert('hamstring')
t.insert('hemlock')
t.insert('headbanger')
t.insert('helicopter')
t.insert('hit')
t.insert('hittite')
t.insert('highrise')
t.insert('hold')
t.insert('hot')
t.insert('hound')
t.insert('hull')
t.insert('huckleberry')
t.insert('humor')
t.insert('hymn')

t.insert('band')
t.insert('bit')
t.insert('bat')
t.insert('ball')
t.insert('bite')
t.insert('bold')

t.insert('cold')
t.insert('cat')
t.insert('can')
t.insert('cannot')
t.insert('call')



def assert_equal(x, y):
    #print(x)
    #print(y)
    if x == y:
        print("PASS")
    else:
        print("FAIL")
        print(x)
        print(y)


#print(t.search('h').children.keys())
#print(t.root.id)
#print(t.root.children)
#print(t.root.children['h'].id)
#print(t.root.children['h'].children)
t.traverse_bfs()
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
