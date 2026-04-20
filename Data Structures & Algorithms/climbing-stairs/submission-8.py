class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonachi dp problem
        # top down to bottom up

        #to climb to stair x we have waysToStair(x-1) + waysToStair(x-2)

        # then just have a base case of x == 1 or x == 2
        # memo = {}

        # def dp(i):
        #     if i <= 2:
        #         return i
        #     if i in memo:
        #         return memo[i]
        #     val = dp(i-1) + dp(i-2)
        #     memo[i] = val

        #     return val
        
        # return dp(n)

        # bottom up it only dependso n the last two values

        # 3: 1 + 2
        # 4: 3 + 2
        # 5: 5 + 3
        if n <= 2:
            return n
        
        # we know its >= 3
        v1, v2 = 1,2
        for i in range(2,n):
            # print("hi")
            v3 = v1 + v2
            v1 = v2
            v2 = v3
        return v2


            
