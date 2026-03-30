class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(n^2)
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # check rows
        for rowNum in range(0, 9):
            for colNum in range(0, 9):
                val = board[rowNum][colNum]
                if val ==".":
                    continue
                key = (int(colNum/3), int(rowNum/3))
                # check if its inside of any of the hashmaps already then reutrn
                if val in row[colNum] or val in col[rowNum] or val in squares[key]:
                    print(str(rowNum) + " " + str(colNum))
                    return False

                row[colNum].add(val)
                col[rowNum].add(val)
                
                # # 0-2, 0-2
                # print(str(key) + " for " + str(rowNum) + " " + str(colNum))
                squares[key].add(val)

        # check the columns


        # check blocks
        return True

