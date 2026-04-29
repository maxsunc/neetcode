class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pass for O(1) is simple
        # keep 3 varaibles one for 0,1,2
        # count the number of 0s,1s,2s
        # then put them in order in nums
        occ = [0,0,0]
        for num in nums:
            occ[num] += 1
        j = 0
        for i in range(0, len(nums)):
            while occ[j] == 0:
                j += 1
            nums[i] = j
            occ[j] -= 1
        



        #O(n) O(1) time, space respectively

        # O(N), O(1) time, space for one pass: Use two Pointers
        # [0,1,1,2
        
        # [1,0,2]