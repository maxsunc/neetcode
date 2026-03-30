class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in myDict:
                return [myDict[complement], i]
            myDict[num] = i