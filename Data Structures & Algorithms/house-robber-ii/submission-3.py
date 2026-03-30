class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def hRob(arr):
            r1,r2 = 0, 0

            for i in range(0, len(arr)):
                temp = max(r1 + arr[i], r2)
                r1 = r2
                r2 = temp
            return r2
        return max(hRob(nums[1:]), hRob(nums[0:len(nums)-1]))