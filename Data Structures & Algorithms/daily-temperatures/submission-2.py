class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #  30,38,30,36,35,40,28\
        # stack
        # Monotonic stack
        # 
        # live problem
        stack = [] # tuples
        result = [0] * len(temperatures)
        # start the stack off
        stack.append((temperatures[0], 0))
        # our stack will keep trackof decreasing values
        for i in range(1,len(temperatures)):
            currentTemp = temperatures[i]
            # if our value is less than or equal the last vlaue we add it to the 
            # if its bigger we will keep popping our stack until the soluton is met
            # O(n) time because we're just iterating through the array once.
            # the worst case is we pop twice, O(2n)
            # check if its greater than our stack value
            # 30,38,30,36,35,40,28
            # [38, 30,]
            # result = [1, 1]
            diff = 1
            while(len(stack) > 0 and stack[-1][0] < currentTemp):
                print(f"comparing {stack[-1]} to {currentTemp} replacing result at {i-diff}")
                # the current value is larger than currentTemp we should reduce our stack and add to result
                pair = stack.pop()
                index = pair[1]
                # diff is used to add to result
                result[index] = i- index
            # add it to the stack cuz we' now looking at 
            # we can add it because we' guarunteed the top of the stack value is either equal 
            # to stack.peek() OR greater than stack.peek()
            stack.append((currentTemp, i))
            print(f"appended {stack[-1]} to stack {stack}")

        return result

