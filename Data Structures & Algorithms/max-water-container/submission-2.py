class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find the maximum amount of water we can store


        # converging 2 pointers

        # returns the max array

        # formula for max arra between 2: min(heights) * (r-l)


        # the idea, there is a bottle neck

        # increment the heights pointer to the shortest one

        l,r = 0, len(heights) - 1
        res = 0
        while r > l:
            res = max(res, min(heights[l], heights[r]) * (r-l))

            # increment the shortest one
            if heights[l] > heights[r]:
                # right is the bottleneck
                r -= 1
            else:
                l += 1
        
        return res
