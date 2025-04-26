import uuid

class TrieNode:
    nodeId = 0

    def __init__(self):
        self.children = {}
        self.id = TrieNode.nodeId
        TrieNode.nodeId += 1
