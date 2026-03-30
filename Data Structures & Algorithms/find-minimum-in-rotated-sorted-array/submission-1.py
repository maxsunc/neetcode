class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]

        # find pivot index
        # return nums[(pivot + 1) % len(nums)]


        l,r = 0, len(nums) - 1
        pivot = 0
        while r >= l:
            m = (r+l) // 2
            
            if nums[m] >= nums[r]:
                pivot = m
                print("pivot changed to " + str(nums[pivot]))
                l = m + 1
            else:
                r = m 

        return nums[(pivot) % len(nums)]