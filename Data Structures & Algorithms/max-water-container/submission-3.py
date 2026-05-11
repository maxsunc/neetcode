class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we want ot find the container with most water

        # is the input guarunteed to be valid
        # there are no negative right?
        # what do we return if the input is nothing? just 0?

        # brute force O(N^2): Check every single sub array 

        # Two Poijnter (O(N)) think of a bottle neck
        # justl ooking for the highest value in the heights

        # two converging pointers

        l,r = 0, len(heights)-1
        res = 0
        while r > l:
            res = max(res, min(heights[r],heights[l]) * (r-l))

            if heights[r] > heights[l]:
                # l is the bottle neck so move it down
                l += 1
            else:
                # r is bottleneck
                r -= 1
        
        return res
