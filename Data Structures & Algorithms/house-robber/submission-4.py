class Solution:
    def rob(self, nums: List[int]) -> int:
        # can't rob the adjacent houses when robbing a house

        # two choices: rob this house or that house

        # if we rob the house we skip the i to + 2
        # if dont rob just look at the next value
        # keep the track of the curVal
        memo = {}
        def dfs(i):
            if len(nums) <= i:
                return 0
            
            if i in memo:
                return memo[i]
            # return max amount you can rob at a house
            val =  max(dfs(i + 1), dfs(i + 2) + nums[i])
            memo[i] = val
            return val

        return dfs(0)