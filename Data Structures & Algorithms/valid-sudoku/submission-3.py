class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # determine whether the board is valid 
        # rows must be 1-9 without duplicates
        # cols must be 1-9 without duplicates
        # sub-boxes must have no duplicates

        rows = defaultdict(set) 
        cols = defaultdict(set)
        grid = defaultdict(set)       

        # iterate through the whole grid

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                val = board[i][j]

                if val == ".":
                    continue

                coord = (i//3) + 3 * (j // 3) 
                if val in rows[i] or val in cols[j] or val in grid[coord]:
                    return False
                
                # add then
                rows[i].add(val)
                cols[j].add(val)
                grid[coord].add(val)
        
        return True