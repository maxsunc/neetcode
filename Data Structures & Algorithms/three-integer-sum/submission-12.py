class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort for free
        # O (n^2) solution
        # 
        nums.sort()
        res = set()
        # for each value look for pairs that add up to -nums[i]
        for i in range(0, len(nums)):
            val = nums[i]
            target = -val
            l,r = i + 1, len(nums) - 1
            while r > l:
                summed = nums[l] + nums[r] 
                if summed == target:
                    res.add((nums[i],nums[l],nums[r]))
                    # look at new elements
                    r -= 1
                    l += 1
                elif summed > target:
                    r -= 1
                else:
                    l += 1
        return list(res)
