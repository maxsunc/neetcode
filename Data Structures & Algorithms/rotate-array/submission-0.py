class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotate an array
        # [1,2,3,4,5,6,7,8] --> [5,6,7,8,1,2,3,4]

        # what if k value is greater than nums length? do we overlap?
        # always rotating to the right
        
        # apply offset of k to each element

        # create a new array of length nums
        copyNums = []
        for val in nums:
            copyNums.append(val)
        # foreach value add k and mod by the length so we dont overshot
        for i in range(0, len(nums)):
            newIndex = (i+k) % len(nums)
            nums[newIndex] = copyNums[i]
        # that is the new posiiton for that element
