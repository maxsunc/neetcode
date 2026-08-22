class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # math: how to find the permiter of an island?

        # look at each land cell:
        # look in all directions: if there is water in a direction or its out of bounds then add to permiters:
        # if there is land, go to that place and call dfs/bfs dont add to permiter
        n,m = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        res = 0
        seen = set()

        def dfs(i,j):
            nonlocal res
            nonlocal n
            nonlocal m
            if grid[i][j] == 0:
                return 
            if (i,j) in seen:
                return
            seen.add((i,j))
            
            # here is a land block
            # look in all directions of this block
            for dir in directions:
                newI, newJ = i + dir[0], j + dir[1]
                if (newI >= n or newJ >= m or newI < 0 or newJ < 0 )or grid[newI][newJ] == 0:
                    # this is water or out of bounds
                    res += 1
                else:
                    # this is land:
                    dfs(newI, newJ)
        for i in range(n):
            for j in range(m):
                if (i,j) not in seen:
                    dfs(i,j)
        return res
