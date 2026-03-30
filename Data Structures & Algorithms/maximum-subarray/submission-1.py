class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # subarray with the largest sum and return it 
        # if adding the value to the curSum makes it overallnegative and start a new

        # [2,-3,4,-2,2,1,-1,4]
        # 


        reze = max(nums)
        curSum = 0
        for i in range(0, len(nums)):
            val = nums[i]

            if curSum + val <= 0:
                # just start a new since its overall negative
                curSum = 0
            elif curSum + val > 0:
                # its overall positive
                curSum += val
                reze = max(reze, curSum)
        return reze
