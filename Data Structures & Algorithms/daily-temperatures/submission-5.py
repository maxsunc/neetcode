class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # find the next greater element:
        result = [0 for i in range(0, len(temperatures))] 

        # monotonic stack

        # keep a stack: the stack is just keeping index of the temperature along iwth the temperature

        stack = []
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                # remove from it
                entry = stack.pop()
                result[entry[0]] = i - entry[0]
            # append to the stack
            entry = (i, temp)
            stack.append(entry)
        
        return result