class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # find the subarray with the largest product within the array and return it
        # return the largest product
        # kadane's algorithm: Starting an new subarray or extending
        
        curMax = 1
        curMin = 1
        res = nums[0]

        # negative * negative = positive
        # negative * positive = negative (update min with this)
        # positive * positive = positive
        for i in range(0, len(nums)):
            # start a new subarray if curMax is negative 
            c1 = nums[i] if nums[i] != 0 else 0
            c2 = curMin * nums[i]
            c3 = curMax * nums[i]

            curMax = max(c1,c2,c3)
            print(curMax)
            curMin = min(c1,c2,c3)
            res = max(res,curMax)

            # [1,2,-3,4]
        return res
