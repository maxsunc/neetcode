class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # look for the corner pieces
        # once you find a corner piece you can only move down or right


        # explore dfs

        # this is a O(N^2) solution

        # is it always non-empty?

        # matrix values are strings right?

        # return the area of the largest square we can find

        # empty isn't possible

        # dfs algorithm

        # O(n * m)

        # (r,c)
        if len(matrix) == 0:
            return 0
        # look for squares with the top left corner and measure squares like that:
        row, col = len(matrix), len(matrix[0])

        # 2 x 2

        # down, right, diagonal

        # min()
        # memoization to not repeat work
        memo = {}
        
        def dfs(r,c):
            if r >= row or c >= col:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]

            if matrix[r][c] == "0":
                return 0 # can't make a square starting from here
            
            # foreach column: find the down length, right length and diagonal length
            down,right,diagonal = dfs(r, c + 1), dfs(r + 1, c), dfs(r + 1, c + 1)

            minSide = min(down,right,diagonal)

            maxDimension = minSide + 1 # because we're 1 on this current tile
            memo[(r,c)] = maxDimension
            return maxDimension


            # find the min of them
        # call this on every 1 we see

        # O(N * M): 
        # O(N * M)

        res = 0
        for i in range(0, row):
            for j in range(0,col):
                res = max(res, dfs(i,j))
        return res * res


            # memoization solution o we don't repeat work

