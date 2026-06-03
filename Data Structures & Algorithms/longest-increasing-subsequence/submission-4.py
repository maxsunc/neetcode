class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # how do we find an increase subsequence?
        # need to keep track of the prev value
        # backtracking problem

        # each value is either take or dont take

        # cna only take if the value is greater than prev

        memo = {}
        def bakctrack(prev,i):
            if i >= len(nums):
                return 0
            if (prev,i) in memo:
                return memo[(prev,i)]

            # retrn the largest increasing subsequence
            val = 0
            if nums[i] > prev:
                # explore branch to take it
                val = bakctrack(nums[i], i + 1) + 1
            sol = max(bakctrack(prev, i + 1), val)
            memo[(prev,i)] = sol
            return sol
        return bakctrack(-1001, 0)