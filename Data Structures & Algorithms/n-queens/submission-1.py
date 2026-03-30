class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtracking problem

        # 
        def convertBoard(board):
            res = []
            for i in range(0, n):
                curStr = ""
                for j in range(0,n):
                    curStr += "Q" if board[i][j] == "Q" else "."
                res.append(curStr)
            return res

        def convertBoardString(board):
            res = ""
            for i in range(0, n):
                for j in range(0,n):
                    res += "Q" if board[i][j] == "Q" else "."
            return res

        def isValidCoord(i, j):
            return 0 <= i < n and 0 <= j < n
        def isValid(board, posQ):
            # check whether board is valid (see if each Q isnt hitting any other guy)
            # given the position of a queen check whether it is touching other queens within the board or not
            # check horizontal (posQ[0] stays constant)
            for i in range(0, n):
                if i != posQ[1] and board[posQ[0]][i] == "Q":
                    return False
            # vertical
            for i in range(0, n):
                if i != posQ[0] and board[i][posQ[1]] == "Q":
                    return False

            # check diagonal one
            directions = [[1,1],[-1,1],[-1,-1],[1,-1]]
            for dir in directions:
                curCoord = (dir[0] + posQ[0], dir[1] + posQ[1])
                while isValidCoord(curCoord[0], curCoord[1]):
                    # its valid we can check it and update it
                    if board[curCoord[0]][curCoord[1]] == "Q":
                        return False
                    curCoord = (dir[0] + curCoord[0], dir[1] + curCoord[1])
            
            return True

        

        unique = set()
        res = []
        # to speed this up keep track of hte row we placed the guy, place one queen per row
        def backtrack(board, queensLeft, row):
            s = convertBoardString(board)
            if queensLeft == 0 and s not in unique:
                
                # convert board to 1d array of strings
                unique.add(s)
                res.append(convertBoard(board))
                return
            
            # we still have some queens left so lets check all positions until its valid
            # go through each of the squares and see if can
            
            for j in range(0, n):
                if board[row][j] == "Q":
                    continue
                # place the queen here and if its valid lets proceed with it
                board[row][j] = 'Q'
                # check if its valid
                posQ = (row,j)
                if isValid(board,posQ):
                    # print(f"valid for board {board}")
                    queensLeft -= 1
                    row += 1
                    # print(f"valid for {board}")
                    backtrack(board, queensLeft, row)
                    queensLeft += 1
                    row -= 1
                # backtrack to test new cases
                board[row][j] = ""
        board = [[""] * n for i in range(0,n)]
        backtrack(board, n,0)

        return res
            
