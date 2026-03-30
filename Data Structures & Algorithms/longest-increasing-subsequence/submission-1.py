import sys
sys.setrecursionlimit(5000)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # strictly increasing subsequence
        # sliding window?"??
        
        # either take or dont take 
        # thats the power of subsequence
        # [9,1,4,2,3,3,7]. 
        # keep track of the prev element, if it isn't bigger then skip
        # if it is bigger then go two ways, skip or take and replace prev
        # this is a very slow way of doibgn it O(2^n * n)

        # one way of making this faster is storing by (i,prev) what was seen before 
        # then we could just add that if 
        memo = {}
        # memoization
        # choose to take or not to take if its greater than prev
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]
            val = dfs(i + 1, prev)
            prevVal = nums[prev] if prev >= 0 else -1001
            if nums[i] > prevVal:
                val = max(val, 1 + dfs(i + 1, i))
            memo[(i,prev)] = val
            return val
        
        return dfs(0, -1)

