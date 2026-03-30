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
        # for i in range(0, len(heights)):
        #     minH = heights[i]
        #     l, r = i - 1, i + 1
        #     width = 1
        #     # move to left for values >= minH
        #     while l >= 0 and heights[l] >= minH:
        #         width += 1
        #         l -= 1

        #     # move to the right for value >= minH
        #     while r < len(heights) and heights[r] >= minH:
        #         width += 1
        #         r += 1
            
        #     res = max(res, minH*(width))


        # use a stack

        # stack stores the current heights

        stack = []

        #  iterate through heights from left to right see if we can extend
        for i in range(0, len(heights)):
            height = heights[i]
            if not stack:
                stack.append((i,height))
            else:
            # Case 1: append to the stack if the value is strictly greater than us (guarunteed will have a bigger unit)
                if height >= stack[-1][1]:
                    # calculate the result that could have occured
                    res = max(res, stack[-1][1] * (i - stack[-1][0] + 1))
                    if height != stack[-1][1]:
                    # append to the stack the new starting point
                        stack.append((i, height))
                    print(stack)
                elif height < stack[-1][1]:
                    # pop all bars larger than us and we can inherit the last popped start positon but must
                    # keep the height the same
                    lastPopped = stack[-1]
                    while stack and stack[-1][1] > height:
                        # calculate the result the max area that could have created
                        res = max(res, stack[-1][1] * (i - stack[-1][0]))
                        # keep popping 
                        lastPopped = stack.pop()
                    # we have the popped stack inherit the index of it and append
                    newEntry = (lastPopped[0], height)
                    stack.append(newEntry)
        for i in range(0,len(stack)):
            res = max(res, stack[-1][1])
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            if not stack:
                stack.append((i,height))
            else:
            # Case 1: append to the stack if the value is strictly greater than us (guarunteed will have a bigger unit)
                if height > stack[-1][1]:
                    # calculate the result that could have occured
                    res = max(res, stack[-1][1] * ( stack[-1][0] - i + 1))
                    # append to the stack the new starting point
                    stack.append((i, height))
                    print(stack)
                elif height < stack[-1][1]:
                    # pop all bars larger than us and we can inherit the last popped start positon but must
                    # keep the height the same
                    lastPopped = stack[-1]
                    while stack and stack[-1][1] > height:
                        # calculate the result the max area that could have created
                        res = max(res, stack[-1][1] * ( stack[-1][0] - i))
                        # keep popping 
                        lastPopped = stack.pop()
                    # we have the popped stack inherit the index of it and append
                    newEntry = (lastPopped[0], height)
                    stack.append(newEntry)

                
            # also update result

            # case 2: If the height is less than the top element on the stack: Append to the stack

        for i in range(0,len(stack)):
            res = max(res, stack[-1][1])
        
        return res


        # how can we optimize this?
        # whenever it meets a value less than the current height we discard

        # [7,1,7,2,2,4]

        # [7,1,1,1,1,1] minFromLeft
        # [1,1,2,2,1,4] minFromRight

        # compute both ways

        # minH * width

        # min values from the left and right

        # monotonic stack

        # 
        

        