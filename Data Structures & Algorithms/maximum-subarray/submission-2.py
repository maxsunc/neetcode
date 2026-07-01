class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # find the subarray with the largest sum and return the sum
        # find a subarray where the sum is the maximum

        # teh elemetns can be negative values right?

        # 1st: approach is brute force: Try all sub arrays which is O(N^2)


        # 2nd: keep track of a the currentSUm
        # we would add values to it on each iteration through nums
        # if the currentSum ends up being negative then reset it to 0 
        

        # iterate throguh nums
        # check if curSum is negative then reset it
        # add to curSum
        # update result if needed O(N)
        curSum = 0
        res = nums[0]
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            res = max(res, curSum)
        return res
