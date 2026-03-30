class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        l, r = 0, len(heights)-1
        maxHeight = 0
        while r > l:
            maxHeight = max(min(heights[l], heights[r]) * (r-l), maxHeight)

            # move the minimium pillar forward (kill the bottleneck)
            if heights[r] <= heights[l]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1

        return maxHeight


