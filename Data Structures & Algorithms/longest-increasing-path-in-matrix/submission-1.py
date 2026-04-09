class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs at every single node
        n = len(matrix)
        m = len(matrix[0])
        # with memoization so it goes faster

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def isValid(i,j):
            return 0 <= i < n and 0 <= j < m
        seen = set()
        memo = {}

        # [1,2,3],
        # [2,1,4],
        # [7,6,5]
        def dfs(i,j):
            # base case: 
            if (i,j) in seen:
                return 0
            seen.add((i,j))
            if (i,j) in memo:
                return memo[(i,j)]
            length = 1

            for dir in directions:
                newI = i + dir[0]
                newJ = j + dir[1]
                if not isValid(newI,newJ):
                    continue
                if matrix[i][j] < matrix[newI][newJ]:
                    # explore this branch and see how big it gets
                    length = max(length, 1 + dfs(newI,newJ))
                    seen.remove((newI,newJ)) # backtracking step
            memo[(i,j)] = length
            return length
        
        maxVal = 0
        for i in range(0,n):
            for j in range(0,m):
                maxVal = max(maxVal, dfs(i,j))

                seen.clear()
        return maxVal



        
        # [1,2,3]
        # [4,5,6]
        # [7,8,9]