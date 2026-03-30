class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [2*4*6, 1*4*6, 1*2*6]
        
        # two stages

        # make a prefix variable
        # iterate through the array multiply the prefix with the current num storing the output array


        # suffix pass have suffix = 1
        # iterate in reverse, multi the curernt value in the output with the suffix

        
        output = [1] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        return output
        
