class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # find the sub array with the largest sum and retur nthat sum
        # this is dp because it is kadane's algorithm and kadane's algorithm is a dp algorithm

        # if the sum is negative, start a new: (we can't go any lower)
        if len(nums) <= 0:
            return 0
        
        res = nums[0] # this is the max subarray sum we find

        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            res = max(res, curSum)
        return res
