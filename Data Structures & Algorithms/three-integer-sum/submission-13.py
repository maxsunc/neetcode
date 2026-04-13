class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort for free
        # O (n^2) solution
        # 
        nums.sort()
        res = []
        # for each value look for pairs that add up to -nums[i]
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip duplicates
            val = nums[i]
            target = -val
            l,r = i + 1, len(nums) - 1
            while r > l:
                summed = nums[l] + nums[r] 
                if summed == target:
                    res.append([nums[i],nums[l],nums[r]])
                    # look at new elements
                    oldVal = nums[l]
                    r -= 1
                    l += 1
                    # get rid of duplicates
                    while l < r and nums[l] == oldVal:
                        l += 1
                elif summed > target:
                    r -= 1
                else:
                    l += 1
        return res
