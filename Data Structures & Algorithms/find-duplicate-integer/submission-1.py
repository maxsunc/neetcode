class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # have an array of ints nums
        # we have n + 1 ints
        # each is in the range [1,n]

        # every int appearso nly once except one integer which appears more than once, we want to find that integer

        # all the solutions below wont use any extra space

        # brute force O(n^2) for each element check if there is a duplicate if there is
        # then return that
        # numbers dont need to be continously increasing

        # find the duplicate nnumber within the array in O(n) time and O(1) space
        # elements are in a range from 0 to n
        # use the array it self as a hashmap

        # so we have up to n + 1 integers
        # while our integers are in the range from 1 to n
        # this means n is a valid nidex!


        # everytime we find a value in the array use that value as the index
        # take the abs of each value so the hashing method wont break the iteration
        # make the value at that index negative meaning we already saw it once
        # if we encounter another value that points to a negative we found the duplicate


        for val in nums:
            ab = abs(val)
            if nums[ab] < 0:
                # its negative so lets return this
                return ab
            nums[ab] *= -1
        return -1


