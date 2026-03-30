class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # continous four-directionally connected group of '0' it is considered surrounded

        # change all surrounded '0's into X's 
        # do they need to a group connected?
        
        # any 0 on the edge cannot be surrounded dont event check the edges
        if len(board) <= 2 and len(board[0]) <= 2:
            return
        

        n,m = len(board),len(board[0])
        # identify the area of O's
        # identify the surrounding area whether they're all x's or not
        # four directionally connected group of '0's 
        # as long as a group is completely enclosed by X's then it is surrounded. 
        # If any O reaches the then that whole group is safe
        # diagonals do not matter
        # only up,left,right,down directions of X's then you're okay

        # in other words we could just look for O's like islands and if it ends up going to the edge's then that whole group isn't valid
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # can eitherb e an O or X right so just check for whether a group of O's will get to an edge or not
        seen = set()
        oSet = set()
        surrounded = True

        def isValid(i,j):
            return 0 <= i < n and 0 <= j < m
        def onBorder(i,j):
            return i == 0 or i == n-1 or j == 0 or j == m-1


        def dfs(i,j): # returns true if it hits a border, false otherwise
            if (i,j) in seen:
                return
            # explores all O's and returns a set of O positions grouped together
            if board[i][j] == "O":
                seen.add((i,j))
                oSet.add((i,j))
                if onBorder(i,j):
                    print(f"{(i,j)} on border")
                    nonlocal surrounded
                    surrounded = False
                # explore other opportunities
                for dir in directions:
                    newI = i + dir[0]
                    newJ = j + dir[1]
                    if isValid(newI,newJ) and board[newI][newJ] == "O":
                        # explore that node
                        dfs(newI,newJ)
        # foreach O seen lets call dfs on it if its not seen yet
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if not (i,j) in seen and board[i][j] == "O":
                    # havent encountered this island yet lets explore
                    dfs(i,j)
                    if surrounded:
                        print(oSet)
                        # for all positions in oSet set them to X
                        for coord in oSet:
                            board[coord[0]][coord[1]] = "X"
                    # reset the set and the surrounded flag
                    surrounded = True
                    oSet = set()
        
        

        






