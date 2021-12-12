import collections

class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for w in word:
            current = current.children[w]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False

        return True



