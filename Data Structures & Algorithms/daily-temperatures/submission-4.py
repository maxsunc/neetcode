class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # find the next day the ith day is warmer 
        # if there is no more warmer day then ur cooked

        # monotonic stack

        # keep a running stack of the 
        stack = []
        res = [0] * len(temperatures)

        # stack stores elemnt looking for a nex smallest
        for i in range(0, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                # this is the next warmers place so append this
                entry = stack.pop()
                print(f"{entry} with {i}")
                length = i - entry[1]
                res[entry[1]] = length 
            # append to the stack
            newEntry = (temperatures[i], i)
            stack.append(newEntry)


        
        return res