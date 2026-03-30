class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chars = {}

        for num in nums:
            chars[num] = 1
        res = 0
        
        for key in chars:
            curLength = 0
            value = key
            if value - 1 not in chars:
                while value in chars:
                    curLength += 1
                    value += 1
                    res = max(res,curLength)
        
        return res
        