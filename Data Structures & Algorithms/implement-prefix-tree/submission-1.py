class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


    def insert(self, word: str) -> None:
        curNode = self
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = PrefixTree()
            # move to the node
            curNode = curNode.children[c]
        curNode.endOfWord = True
        


    def search(self, word: str) -> bool:
        curNode = self
        for c in word:
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        return curNode.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        # looking for whether a previously inserted word has prefix
        # this is just search, but opposite check for endOfWord?        
        curNode = self
        for c in prefix:
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        return True