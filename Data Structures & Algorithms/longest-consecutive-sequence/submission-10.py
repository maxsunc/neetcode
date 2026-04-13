class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the starting point of each sequence and explore that only 
        
        s = set(nums)
        res = 0
        for n in nums:
            curLength = 1
            if not n-1 in s:
                # this is the start
                val = n + 1
                while val in s:
                    val += 1
                    curLength += 1

            res = max(curLength, res)
        
        return res
                
