class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # find 3 numbers that sum up to 0
        # sort for freee
        # foreach value do a two sum on a sorted list iwth 2 pointer
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            # skip duplicates
            if i > 0 and nums[i-1] == num:
                continue
            target = -num
            l,r = i + 1, len(nums) - 1
            while r > l:
                curSum = nums[l] + nums[r]
                if curSum == target:
                    res.append([num,nums[l],nums[r]])
                    r -= 1
                    l += 1
                    while l < len(nums) and nums[l-1] == nums[l]:
                        l += 1
                elif curSum > target:
                    r -= 1
                else:
                    l += 1
        return res
                    # [-4,-1,-,1,0,1,2]
