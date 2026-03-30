class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # with the trick for 3 sum is that we can sort the array for free :)

        # nlogn 
        nums.sort()
        print(nums)

        # for each value we do two pointers on it to find newTarget (newTarget = target - curVal)
        res = []
        for i in range(0, len(nums) - 2):
            # skip prevvious values
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = -nums[i]
            # find 2 values that add upt ot it

            l, r = i + 1, len(nums) - 1
            curSum = nums[l] + nums[r]
            while r > l:
                if curSum == target:
                    res.append([nums[r],nums[l],nums[i]])
                    # look at next
                    # move until no more duplicates for left
                    duplicate = nums[l]
                    while len(nums) > l and nums[l] == duplicate:
                        l += 1
                elif curSum > target:
                    r -= 1
                else:
                    l += 1
                # calculate
                if len(nums) > l and 0 <= r:
                    curSum = nums[l] + nums[r]
        

        return res
                
