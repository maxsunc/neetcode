class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # find the number of ways to build target sum
        # its not just adding

        # [1,2]
        # choose to add or subtract

        # memoization solution
        # find the number of ways to become target

        # keep track of curSum and i


        # [2,2,2]
        # each instance is new so if it makes it to the result then just return 

        # Save the number of targets made at each (i,curSum)
        # to pdown
        memo = {}
        def dfs(i, curSum):
            # print(curSum)
            if curSum == target and i == len(nums):
                # print(f"found 1 for {(i,curSum)}")
                return 1 # we found one way
            if i >= len(nums):
                return 0
            if (i,curSum) in memo:
                return memo[(i,curSum)]

            
            val = 0
            # recursive case
            val += dfs(i+1, curSum + nums[i]) + dfs(i+1, curSum - nums[i]) # ways from including or not including
            memo[(i,curSum)] = val
            return val

        return dfs(0,0)
            


