class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        def isValid(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        directs = [[1,0],[-1,0],[0,1],[0,-1]]
        seen = set()
        def dfs(i,j):
            if (i,j) in seen:
                return
            
            seen.add((i,j))
            for dir in directs:
                newI,newJ = i + dir[0], j + dir[1]
                if isValid(newI,newJ) and grid[newI][newJ] == "1":
                    dfs(newI,newJ)
        
        res = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == "1" and not (i,j) in seen:
                    dfs(i,j)
                    res += 1
        return res
