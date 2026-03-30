class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # return True if the word is wtihin the 2d grid
        # False if the word isnt within the grid

        # input always valid?
        # word search !



        # first approach: use a dfs algorithm: function that takes in just an index, row, col
        # index = current character we're looking for 
        # base case: index == len(word) get back true 

        # outside of this loop we want to call our function on each first character matching 
        # if we find the word we can proceed the index + 1, the function will look left right, up down for the character we desire

        # if we find that character call the function on that position wiht index + 1

        # 
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def isValid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def backtrack(index, row, col, seen):
            print(index)
            # base case we case about 
            if index == len(word):
                return True # this word length works
            
            wordExists = False
            oldSeen = seen.copy()
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                print(f"comparing {(newRow,newCol)} with {seen} set")
                if (newRow,newCol) in seen:
                    continue
                # check if the character at newRow and newCol is the same as word[index]
                if isValid(newRow, newCol) and board[newRow][newCol] == word[index]:
                    # it is the same character, let's explore this tile
                    seen.add((newRow, newCol))
                    if backtrack(index + 1, newRow, newCol, seen):
                        # if the backtrack comes back true then this branch is good
                        wordExists = True
                        break
                    else:
                        # invalid so we need to backtack
                        seen = oldSeen
            return wordExists

        firstChar = word[0]
        wordExists = False
        seen = set() # seen coordinates
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                print(board[i][j])
                if firstChar == board[i][j]:
                    seen.add((i,j))
                    if backtrack(1, i, j, seen):
                        return True
                    seen = set() # reset seen
        return False
        
        # ABCE
        # SFCS
        # ABEE


        # ABCE
        # SFES
        # ADEE

