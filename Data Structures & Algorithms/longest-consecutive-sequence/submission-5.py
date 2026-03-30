class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we're only interest in the start of the sequences

        # to check if it is the start of a sequence we do check if num-1 exists



        # build a hashset
        mySet = set(nums)



        # build an array of starting points
        starting = []
        for n in nums:
            if n - 1 not in mySet:
                starting.append(n) # n is a starting place

        



        res = 0
        # iterate thru the starting points see how high they can go and take the max then just retunr that
        for start in starting:
            # increase and see how high we can go
            curVal = start + 1
            while curVal in mySet:
                curVal += 1
            
            res = max(res, curVal - start)

        return res
