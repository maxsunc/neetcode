class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # [1,2,3,4]
        # [1,2,3,4,5]
        # 
        if sum(nums) % 2 == 1:
            return False
        # add to subset 1 or add to subset 2
        totalSum = sum(nums)
        memo = {}
        def dfs(i, sum1):
            if i == len(nums):
                return sum1 == totalSum / 2
            if (i,sum1) in memo:
                return memo[(i,sum1)]
            # recursive case, add to sum1 or add to sum2
            res = dfs(i + 1, sum1) or dfs(i + 1, sum1 + nums[i])
            memo[(i,sum1)] = res


            return res

        return dfs(0,0)
