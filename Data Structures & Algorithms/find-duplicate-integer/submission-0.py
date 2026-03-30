class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use O(1) space (no hashmaps)
        # first solution: Use a set  O(n) space, O(n) time complexity

        # length = n+1
        # from 1 to len - 1 inclusive
        # 2nd solution: elements are within the range from 1 to n = len(nums)

        # use the nums itself as a hashing method
        # the formula: nums[abs(nums[i] - 1)] *= -1
        # if the nums there is already negative then that means we ALREADY visited it, in other words, its a duplicate
        # return that value if that is the case
        # iterate through nums
        for i in range(0,len(nums)):
            # check for duplicates, return value if thats the case
            # because we're only dealing with positive numbers, this hashing method works
            if nums[abs(nums[i]) - 1] < 0:
                # it is already negative, meaning we have seen it before !
                return abs(nums[i])
            # 2. apply the formula
            nums[abs(nums[i]) - 1] *= -1

            

        return -1
        