class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0 for i in range(0,9)] for i in range(0,9) ]
        cols = [[0 for i in range(0,9)] for i in range(0,9)]
        squares = [[0 for i in range(0,9)] for i in range(0,9)]



        for rowNum in range(0,9):
            for colNum in range(0,9):
                if board[rowNum][colNum] == ".":
                    continue
                value = int(board[rowNum][colNum]) - 1

                # check if that value at that point already exists, if so return False
                if rows[rowNum][value] == 1 or cols[colNum][value] == 1:
                    return False
                index = (rowNum//3) + 3 * (colNum//3)
                if squares[index][value] == 1:
                    return False


                # update the places
                rows[rowNum][value] = 1
                cols[colNum][value] = 1
                squares[index][value] = 1

        return True