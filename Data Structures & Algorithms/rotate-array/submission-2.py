class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newArr = [0 for i in range(0, len(nums))]
        # compute the postiions and put them into the new array
        for i, num in enumerate(nums):
            newI = (i + k) % len(nums)
            newArr[newI] = num
        
        for i in range(0, len(nums)):
            nums[i] = newArr[i]
