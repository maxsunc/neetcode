class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # chec each row
        # check each column

        # size: 81 * 3
        # boxes
        # rows
        # columns
        rows = [set() for i in range(0,len(board))]
        cols = [set() for i in range(0,len(board))]
        boxes = [[set() for i in range(0,3)] for j in range(0, 3)] # coords: i // 3, j // 3

        for i in range(0, len(board)):
            for j in range(0,len(board)):
                # check if this is already seen before in the respective positions
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i]:
                    # print(f"row: found  {val} in {rows[i]}")
                    return False

                if val in cols[j]:
                    # print(f"col: found {val} in {cols[j]}")
                    return False
                if val in boxes[i//3][j//3]:
                    # print(f"box: found {val} in {boxes[i//3][j//3]}")
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[i//3][j//3].add(val)
        
        return True
        

