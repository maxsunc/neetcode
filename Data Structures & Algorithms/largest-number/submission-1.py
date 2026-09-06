from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 3,30,34,5,9

        # first value takes presedence over all
        # make another ranking for 2+ length
        allZero = True
        for n in nums:
            if n != 0:
                allZero = False
                break
        if allZero:
            return "0"

        # custom sorting python

        # convert to strings

        # compare the strings by their 
        # straight up glue them together and see how the comparison works:
        def compare(n1,n2):
            n1n2 = n1 + n2
            n2n1 = n2 + n1
            # if n1n2 > n2n1 then n1 wins return true n1 > n2
            if n1n2 >= n2n1:
                return -1 # n1 goes first
            else:
                return 1 # n2 go first

        numStrs = [str(n) for n in nums]

        # sort it according to compare
        # compare with a custom function, this is comparing twovlaues
        numStrs.sort(key=cmp_to_key(compare)) 

        # add it to result
        return "".join(numStrs)