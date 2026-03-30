class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        # stack will keep track of the indicies we look at 
        # compare with the top value of the stack
        # if the current value we are looking at is greater than stack top that means we found a warmer tmeperature
        # pop it off the stack and compare with next value

        stack = []
        res = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                 # we found a smaller value,pop it off the stack
                 val = stack.pop()
                 res[val] = i - val

            # add it to the stack to look for vlaues of this
            stack.append(i)

        while len(stack) > 0:
            # remaining elements are 0
            val = stack.pop()
            res[val] = 0
        return res

