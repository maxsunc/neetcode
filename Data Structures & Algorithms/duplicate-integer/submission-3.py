class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return true if a duplicate exists within the array
        # using a set we can do this in O(n) time
        mySet = set()

        for num in nums:
            if num in  mySet:
                return True
            mySet.add(num)
        return False