class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonachi dp problem
        # top down to bottom up

        #to climb to stair x we have waysToStair(x-1) + waysToStair(x-2)

        # then just have a base case of x == 1 or x == 2
        memo = {}

        def dp(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            val = dp(i-1) + dp(i-2)
            memo[i] = val

            return val
        
        return dp(n)

            
