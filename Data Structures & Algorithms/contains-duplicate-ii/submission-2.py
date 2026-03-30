class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        mySet = set()

        for i in range(k):
            if nums[i] in mySet:
                return True
            mySet.add(nums[i])
        
        for i in range(k, len(nums)):
            if nums[i] in mySet:
                return True
            mySet.remove(nums[i-k])
            mySet.add(nums[i])





        return False