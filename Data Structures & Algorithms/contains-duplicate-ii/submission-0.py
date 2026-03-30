class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mappa = {}

        for i in range(0, len(nums)):
            if nums[i] in mappa.keys():
                if abs(mappa[nums[i]] - i) <= k:
                    return True
            mappa[nums[i]] = i

        return False 