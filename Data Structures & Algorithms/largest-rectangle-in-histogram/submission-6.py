class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, height in enumerate(heights):
            start = i # starting index

            # if we encounter an element less than the top of the stack
            while stack and stack[-1][1] > height:
                # reduce until you can't
                entry = stack.pop()
                # calculate the result
                res = max(res, (entry[1]) * (i - entry[0]))
                # inherit the start position
                start = entry[0]


            # add it to the stack
            stack.append((start, height))
        
        # remainning elements in the stack didnt find something smaller than them 
        # so they got to the end. since our stack is increasing we can go full height on them
        for i in range(0, len(stack)):
            res = max(res, stack[i][1] * (len(heights) - stack[i][0]))
        return res