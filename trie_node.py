import uuid

class TrieNode:
    nodeId = 1

    def __init__(self):
        self.children = {}
        self.id = TrieNode.nodeId
        TrieNode.nodeId += 1
