class WordDictionary:

    def __init__(self):
        # adding new words and searching for existing words
        # we'll need
        self.children = {}
        self.endOfWord = False


    def addWord(self, word: str) -> None:
        # add words to the dictionary
        # check if it already exists or not
        curNode = self
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = WordDictionary()
            curNode = curNode.children[c]
        curNode.endOfWord = True

    def search(self, word: str) -> bool:
        # dot is a wildcard? It can be anything
        # when theres a dot

        # at most 2 dots in searches
        # when we get to a dot. search ALL. children for the remainning stuff
        # if even one returns True then we're good
        # if the word is empty what will happen?
        # I think this needs to be recursive
        # base case: if its empty we return True
        def searchRecur(i, curNode):
            if i == len(word):
                return curNode.endOfWord
            # check if its a wildcard: Then explore all opportunities
            if word[i] == '.':
                for child in curNode.children:
                    if searchRecur(i + 1, curNode.children[child]):
                        return True
            elif word[i] in curNode.children:
                # check if word[i] is in children then explore that
                return searchRecur(i + 1, curNode.children[word[i]])

            return False
        return searchRecur(0,self)
