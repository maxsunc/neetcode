class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # find the number of unique paths from (0,0) to (m-1,n-1)

        # 1. memoization keep track of the number of ways to get to the result from each square

        # 1 again: bottom up approach foreach square document how many possible ways it is to get their

        # usually it would be dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # if dp can support i-1 or j-1
        # basecase if i ==0 and j==0: return 1

        dp = [[0 for i in range(0,n)] for j in range(0,m)]

        dp[0][0] = 1

        for i in range(0,m):
            for j in range(0,n):
                if j != 0:
                    # left
                    dp[i][j] += dp[i][j-1]
                if i != 0:
                    print(f"{i}{j}")
                    dp[i][j] += dp[i-1][j]
        
        return dp[m-1][n-1]
