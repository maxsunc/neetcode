class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # method 1
        # store a set of unique elements
        # add all unique elements and empty that into the nums at the end
        # 

        # 2 pointer method for O(n) time complexity with O(1) space

        # left is 0, right is 1
        # 
        left = 0

        for right in range(1,len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        return left + 1

        # [1,2,3,4,5]

        # move right pointer from 1 to len(nums) -1
        # everytime nums[right] != nums[left]: # this means a new element was found

        # when we find a new element advance left pointer and place new element at posiion of left

        # 