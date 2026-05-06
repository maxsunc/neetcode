class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0 

        for i,height in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > height:
                # pop from the stack
                entry = stack.pop()
                # calculate the stack
                
                res = max(res, entry[1] * (i - entry[0]))
                start = entry[0]

            stack.append((start,height))
        
        # calculate the remaining elmeents
        for i in range(0, len(stack)):
            res = max(res,stack[i][1] * (len(heights) - stack[i][0]))
        return res