class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # with the trick for 3 sum is that we can sort the array for free :)

        # nlogn 
        nums.sort()
        print(nums)

        # for each value we do two pointers on it to find newTarget (newTarget = target - curVal)
        res = set()
        for i in range(0, len(nums) - 2):
            target = -nums[i]
            # find 2 values that add upt ot it

            l, r = i + 1, len(nums) - 1
            curSum = nums[l] + nums[r]
            while r > l:
                if curSum == target:
                    res.add((nums[r],nums[l],nums[i]))
                    # look at next
                    l += 1
                    r -= 1
                elif curSum > target:
                    r -= 1
                else:
                    l += 1
                # calculate
                curSum = nums[l] + nums[r]
        

        return list(res)
                
