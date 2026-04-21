class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left rotated a certain number of times

        # first find the rotated position 
        
        # [4,5,6,7,8,9,10,0,1,2]

        # we want to find the min position in O(logn) time: Use binary search
        # what if that element isnt in the array?: return -1
        

        # if the mid element is greater than the last element that means that mid point is part of the 1st half split: update the left pointer 
        # if the mid element is less than the last element it could be the min value so update the minVal and offsetIndex then we can look further: update the right pointer

        minElement = nums[0]
        minIndex = 0

        l,r = 0, len(nums) - 1
        while r >= l:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                # move the left pointer over
                l = mid + 1
            else:
                if minElement > nums[mid]:
                    print(f"replacing {minElement} with {nums[mid]}")
                    minElement = nums[mid]
                    minIndex = mid
                r = mid - 1

        # print(minIndex)
        offset = minIndex
        # bs with offset
        # apply the transformation at the end?
        l,r = 0, len(nums)-1

        while r >= l:
            mid = l + (r-l) // 2
            newMid = (mid + offset) % len(nums)
            if nums[newMid] == target:
                return newMid
            elif nums[newMid] > target:
                # move r down
                r = mid - 1
            else:
                l = mid + 1
        
        return -1





        
        

        # Phase 1: Find the rotation position (EX: 4)

        # then do normal binary search with that offset

        # this O(2logn) which is just simplified to O(logn)

        # Phase 2: Binary search with offset