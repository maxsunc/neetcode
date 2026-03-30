class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # distinct indicies
        # use a hashmap to keep track of the past occurance of each value
        # int, int
        # 
        mappa = {}

        for i in range(0,len(nums)):
            val = nums[i]
            # update the occurance index
            if mappa.get(val, -1) == -1:
                mappa[val] = i
            else:
                # ISNT the first time we're seeing this
                # check if 
                if i - mappa[val] <= k:
                    return True
                mappa[val] = i
        return False

        

        
        # # 2 distinct indicies i and j such that
        # # nums[i] == nums[j] and the distance is less than or equal to k
        # if k == 0:
        #     return False
        # # fixed sliding window
        # for i in range(0, len(nums)):
        #     for j in range(i+1, min(len(nums),i + k + 1)):
        #         print("comparing " + str(nums[i]) + " with " + str(nums[j]))
        #         if nums[i] == nums[j]:
        #             return True
        
        # return False