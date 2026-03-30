class Solution:
    def climbStairs(self, n: int) -> int:
        # number of distinct steps either 1 or 2 steps each time


        # top to bottom recursion with memoization

        # n = 2

        # 1 + 1 = 2
        # 2 = 2
        res = 0
        # memoization component, store already computed steps

        # def dp(curStep):
        #     nonlocal res
        #     # cannot exceed it
        #     if curStep == n:
        #         res += 1
        #         return 
        #     elif curStep > n:
        #         return # overstepped not valid
            
        #     # check all posibilities (backtracking)
        #     dp(curStep + 1)
        #     dp(curStep + 2)
        # dp(2)
        # dp(1)

        # bottom up tabulation solution
        # calculate the ways you can get to a staircase then 
        # draw the recureence
        # base case: ways(1) = 1
        # ways(2) = 2
        if n < 2:
            return n
        # if n > 2: ways(n) = ways(n-1) + ways(n-2)
        # ways = [0 for i in range(0, n)]
        # ways[0] = 1
        # ways[1] = 2

        # # calculate from bottom up in this case
        # for i in range(2, len(ways)):
        #     ways[i] = ways[i-1] + ways[i-2]

        # recursive solution:
        # save the result of calculated values
        ways = [0 for i in range(0, n+1)]
        ways[0] = 1
        ways[1] = 2
        def dp(i):
            # base cases
            if i <= 2:
                return i
            # recursive case
            if ways[i] != 0:
                return ways[i]
            val = dp(i-1) + dp(i-2)
            ways[i] = val
            return val

        return dp(n)
