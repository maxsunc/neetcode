class Solution:
    def climbStairs(self, n: int) -> int:
        # n = number of steps to reach the top of a staircase:
        # climb with either 1 or 2 steps at a time
        # how many ways are there to reach staircase n


        # top down approach
        memo = {}

        def dp(curStair):
            if curStair == n:
                return 1
            if curStair > n:
                return 0 
            if curStair in memo:
                return memo[curStair]    

            res = dp(curStair + 1) + dp(curStair + 2)
            memo[curStair] = res
            return res
        return dp(0)