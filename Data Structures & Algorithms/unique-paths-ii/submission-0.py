class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # backtracking problem to get all possible paths
        # except if we encounter a rock return 0 immmediantly

        # can ony move right or down
        # to speed this up we could try memoization
        # since ight down and down right are the same thing essenially
        memo = {}
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        # print(f"{n}, {m}")
        def backtrack(i,j):
            if obstacleGrid[i][j] == 1:
                return 0 # end this since its an obstacle
            if i == m - 1 and j == n - 1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            
            tracked = 0
            if i + 1 < m:
                # explore right
                tracked += backtrack(i + 1, j)
            if j + 1 < n:
                tracked += backtrack(i,j + 1)
            memo[(i,j)] = tracked
            return tracked
        
        return backtrack(0,0)


