class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we have an array of heights

        # where each heights[i] is the height of a bar

        # each width is 1

        # we want to find the largest area that can be made among the bars

        # 
        #
        ###
        ####

        # brute force solution 

        # [4,2,1]

        # this is the smallest height

        # for each value with in the array


        # check whether we can extend to the left (is it bigger or smaller than us there?)
        res = 0
        # same for the right side
        for i in range(0, len(heights)):
            minH = heights[i]
            l, r = i - 1, i + 1
            width = 1
            # move to left for values >= minH
            while l >= 0 and heights[l] >= minH:
                width += 1
                l -= 1

            # move to the right for value >= minH
            while r < len(heights) and heights[r] >= minH:
                width += 1
                r += 1
            
            res = max(res, minH*(width))
        
        return res

        