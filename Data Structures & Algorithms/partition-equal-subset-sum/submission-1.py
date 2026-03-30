class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # parittion into subset 1 and subset 2 such that their sums are equal

        # [1,2,3,4,5]
        # 8
        # 7

        # sort and add to the smaller one
        # [1,2,3,4]
        # 4
        # 5

        # [1,2,3,6]
        
        # sum1,sum2 = 0,0

        # nums.sort()

        # for i in range(len(nums)-1, -1, -1):
        #     if sum1 >= sum2:
        #         sum2 += nums[i]
        #     else:
        #         sum1 += nums[i]
        
        # return sum1 == sum2

        # we want to build a subset of an array with a sum equal to half the sum exactly
        # im stupid bro wrtf

        # if the sum is odd we can return false
        if sum(nums) % 2 == 1:
            return False
        # [1,2,69]
        desireSum = sum(nums) // 2 # sum we want to get to
        # find a subsequence in array with the sum of desireSum
        memo = {}
        # to take or not to take
        # when the curSum is desireSum then return True
        # if its greater then return False
        def dfs(i, curSum):
            nonlocal desireSum
            if curSum == desireSum:
                return True
            elif curSum > desireSum:
                return False # early return sinceo nly +ve values
            # base cases:
            if i == len(nums):
                return False
            if (i,curSum) in memo:
                return memo[(i,curSum)]
                # at the end and didnt reach desireSum
            result = dfs(i + 1, curSum) or dfs(i + 1, curSum + nums[i])
            memo[(i,curSum)] = result
            # backtracking cases
            return result
        
        return dfs(0, 0)




        # to take or not to take

