class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # find all triplets where they are distinct and the numbers sum up to 0
        # brute force approach is O(N^3) find all triplets in the thing

        # we need to return distinct triplets as well: we're returning triplets
        # clarifying questions:
        # O(N^2) approach maybe?
        # first sort the array: nlogn
        # for each of the elements within the array do two pointer on the remainning elements to determine 
        # which two elements have a sum of -nums[i]
        # skip duplicates? keep track of the prev value and skip those
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -val
            # use two pointers 
            l, r = i + 1, len(nums) - 1
            while r > l:
                # search for the sum of target
                summed = nums[l] + nums[r]
                if summed == target:
                    res.append([nums[i],nums[l],nums[r]])
                    duplicate = nums[l]
                    while r > l and nums[l] == duplicate:
                        l += 1
                    r -= 1 # this is fine but not needed
                elif summed > target:
                    # reduce from right
                    r -= 1
                else:
                    l += 1
        print(res)
        return res