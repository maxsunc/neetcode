class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the longest consecutive sequence of elements that can be formed?
        # within an array it has a log of consequtive sequences
        

        # want to identify the starting value and start counting from there

        # [2,20,4,10,3,4,5]

        # look for the start of the sequence then check 

        map = set(nums)
        res = 0

        for num in nums:
            # if num -1 is present then skip it (theres a bigger )
            # if its not then we found the starting zone so look after thiat

            # in the worst case this will be O(2N)
            if num - 1 in map:
                continue
            # if it isn't then this i the start so its worth pursuing
            val = num
            while val in map:
                val += 1
            res = max(val - num, res)
        return res
