class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def add(self, word):
        curNode = self
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
        curNode.endOfWord = True
    
    # def search




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # list of strings words
        # return all words present in the grid
        # dfs or bfs to look for values
        # Intuition: seems difficult to look for multiple wordds
        # each iteration we would need to check each character within words
        # this is very slow 

        # are we guarunteed the input is valid always?
        # words only contains unique values?
        # what i f the word appears twioce?: put one in result?
        # the best data structure to use for this: trie
        # 1. build our prefix tree so we can traverse it
        # make a data structure
        # 
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        root = TrieNode()
        for word in words:
            root.add(word)
        

        res = set() # avoid duplicates
        # we wanna do dfs on it:  keep track of curNode, i,j, curWord
        # check whetehr the curNode is an endOfWord then add that word we have
        # call dfs on any characters that are in children of bnase:
        
        def isValid(i,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        seen = set()
        def dfs(i,j, curNode, curWord):
            # base case: If the curNode is a endOfWord
            if curNode.endOfWord:
                res.add(curWord)
            seen.add((i,j))
            # recursive case:
            # check around i,j if the children are in curNode.children, lets explore those
            for dir in directions:
                newI,newJ = i + dir[0], j + dir[1]
                if not isValid(newI,newJ):
                    continue
                charToMatch = board[newI][newJ]
                if charToMatch in curNode.children and (newI,newJ) not in seen:
                    # we can explore this to see
                    dfs(newI,newJ, curNode.children[charToMatch], curWord + board[newI][newJ])
            seen.remove((i,j))
        # call dfs on any characters that are in children of base
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                char = board[i][j]
                if char in root.children:
                    dfs(i,j,root.children[char],char)
        return list(res)

