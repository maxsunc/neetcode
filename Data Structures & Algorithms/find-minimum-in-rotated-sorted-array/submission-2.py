class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we want to find the min

        # we just want to find the number of times it was rotated
        # [1,2,3] -> [3,1,2]

        # res = the minimium vlaue
        # [3,4,5,6,1,2]
        # Run binary search but modified

        # r will always be next to l

        # everytime our value is 
        # smaller than or equal to r then we update min val
        # update r vlaue 

        # if the value is greater than r that means we're apart of the 2nd split:
        # update the L value



        # at the end return the min value found

        minVal = nums[0]

        l, r = 0, len(nums) - 1
        m = 0
        while r >= l:
            m = (l + r) // 2
            val = nums[m]
            # case 1
            if val <= nums[r]:
                # move up the r value
                minVal = min(minVal, nums[m])
                r = m - 1
                # case 2;
            else:
                l = m + 1
        
        # [1,2,3,4,5]
        return minVal
            




