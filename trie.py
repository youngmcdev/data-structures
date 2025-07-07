import trie_node
import queue_implementation
import json
from abc import ABC, abstractmethod

class NodeData:
        def __init__(self, nodeId: int):
            self.nodeId = nodeId
            self.children = {}

class Trie:

    def __init__(self):
      self.root = trie_node.TrieNode()
    

    # Search the tree for the value of word. If it exists, return the last node. 
    def search(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None

        return current_node
    

    # Search the tree for the value of word. If it does not exist, add it.
    def insert(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = trie_node.TrieNode()
                current_node.children[char] = new_node
                current_node = new_node

        current_node.children["*"] = None


    # Return an array of all the words that can be generated beginnig at the node 
    # that is passed in (defaults to the root node). 
    def collect_all_words(self, words, node: trie_node.TrieNode = None, word=""):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collect_all_words(words, child_node, word + key)

        return words
    

    # Given the prefix passed in, return a list containing the remaining characters 
    # of all possible words.
    def autocomplete(self, prefix):
        current_node = self.search(prefix)

        if not current_node:
            return None
        
        return self.collect_all_words([], current_node)


    # This is a helper method for travese_bfs(). It aids in displaying the relationships in console output.
    def get_children_node_data(self, node: trie_node.TrieNode): 
        nodeData = NodeData(node.id)
        childData = {}
        for currentChildNodeCharacter, currentChildNode in node.children.items():
            if currentChildNode is None:
                childData[currentChildNodeCharacter] = 'End-of-Word' 
            else:
                childData[currentChildNodeCharacter] = currentChildNode.id
        nodeData.children = childData
        return nodeData


    # Traverse the tree and ouput its contents to the console.
    def traverse_bfs(self):
        startingNode = self.root
        queue = queue_implementation.Queue()
        charactersFromChildNodes = self.get_children_node_data(startingNode).children
        rowsOfCharacters = [{str(startingNode.id): json.dumps(charactersFromChildNodes)}]
        visitedNodes = {}
        visitedNodes[startingNode.id] = True
        queue.enqueue(startingNode)

        while queue.read():
            currentNode = queue.dequeue()
            #childrenNodeData = self.get_children_node_data(currentNode)
            #print(list(childrenNodeData.children.values()))

            nodeDict = {}
            for currentChildNodeCharacter, currentChildNode in currentNode.children.items():
                if currentChildNode is not None and not visitedNodes.get(currentChildNode.id):
                    visitedNodes[currentChildNode.id] = True
                    queue.enqueue(currentChildNode)
                    charactersFromChildNodes = self.get_children_node_data(currentChildNode).children
                    nodeDict[str(currentChildNode.id)] = json.dumps(charactersFromChildNodes)
            
            if len(nodeDict) > 0:
                rowsOfCharacters.append(nodeDict)
        
        for rowOfCharacters in rowsOfCharacters:
            print(rowOfCharacters)
        

    # ??
    def autocorrect(self, word):
        current_node = self.root
        word_found_so_far = ""

        for char in word:
            if current_node.children.get(char): 
                word_found_so_far += char 
                current_node = current_node.children.get(char)
            else:
                return word_found_so_far + \
                    self.collect_all_words([], current_node)[0]

        return word


# Not super useful, but does taverse the tree printing the key of each node.
    def traverse(self, node: trie_node.TrieNode = None):
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            print(key)

            if key != "*":
                self.traverse(child_node)