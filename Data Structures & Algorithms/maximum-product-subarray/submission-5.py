class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # find the subarray that has the largest product within the array and return it!

        # [1,2,-3,4]
        # cant change the order of the array

        # 
        
        # brute force solution: try each and every sub array

        # contigous
        

        # [1,2,-3,4]

        # [1,2,3]

        # min and max product values
        # update when introducing a new element: starting a newSubarray ==> just the value we found
        # mutiplying by prev max product
        # multiplying by prev minProduct

        maxProd, minProd = nums[0],nums[0]
        globalMax = nums[0]
        # [2,3,-2,4]

        for i in range(1, len(nums)):
            # start a new value or multiply by min or max
            oldMax = maxProd
            maxProd = max(maxProd * nums[i], nums[i],nums[i] * minProd)
            minProd = min(oldMax * nums[i], nums[i],nums[i] * minProd)
            globalMax = max(maxProd, globalMax,minProd)
        return globalMax