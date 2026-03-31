class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0

        reze = 0
        while r < len(nums) - 1:
            # get the furthest
            furthestIndexReached = 0

            for i in range(l, r + 1): # from l to r which one can reach the furthest 
                furthestIndexReached = max(furthestIndexReached, nums[i] + i)   
            
            l = r + 1
            r = furthestIndexReached
            reze += 1
        
        return reze