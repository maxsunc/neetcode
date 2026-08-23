class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # brute force: O(N^2) 
        # kadane's alogirthm

        # either it doesn't wrap around or it does wrap around

        # use kadane's algorithm is find the non wrapping pportion

        # for the rapping portion:
        
        # 1,-4,3,5,-1
        if len(nums) <= 0:
            return 0
        total = sum(nums)
        curMax, curMin = 0,0
        globalMax,globalMin = nums[0],nums[0]

        for num in nums:
            if curMax < 0:
                curMax = 0
            if curMin > 0:
                curMin = 0
            
            curMax += num
            curMin += num

            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        print(globalMax)
        if total != globalMin:
            globalMax = max(globalMax, total - globalMin)
        return globalMax

