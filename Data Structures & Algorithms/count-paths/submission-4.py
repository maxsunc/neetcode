class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m by n grid
        # either move down or right
        # backtracking problem: find the number of ways to get to the start
        # each path we explore must be unique

        # (0,0) --> (m-1,n-1)
        
        # recursion: Decision tree

        def isValid(i,j):
            return 0 <= i < m and 0 <= j < n
        memo = {}
        def backtrack(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m - 1 and j == n - 1:
                return 1
            val = 0
            # check to move left or right if its valid
            if isValid(i+1,j):
                val += backtrack(i + 1, j)
            if isValid(i,j+1):
                val += backtrack(i,j + 1)
            memo[(i,j)] = val
            return val
        
        
        return backtrack(0,0)