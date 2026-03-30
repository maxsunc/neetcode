class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target:
            return 0

        result = len(nums)

        curSum = 0

        # sliding window
        left = 0
        for right in range(0, len(nums)):
            
            curSum += nums[right]
            print(curSum)
            while(curSum >= target):
                curSum -= nums[left]
                result = min(result, right - left +1)
                left += 1

        return result



