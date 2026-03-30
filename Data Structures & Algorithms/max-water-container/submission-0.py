class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer
        maxVal = 0 
        i = 0
        j =  len(heights) - 1

        while(j > i):
            value = min(heights[i], heights[j]) * (j-i)
            if(value > maxVal):
                maxVal = value
            if(heights[i] > heights[j]):
                j -= 1
            else:
                i += 1

        return maxVal

        # move in the direction of the shortest pillar
        # [1,7,2,5,4,7,3,6]
        # formula for area of water
        # water = min(heights[i], heights[j]) * (j-i) 
        # look for the bottleneck (shortest one) and move it away 
