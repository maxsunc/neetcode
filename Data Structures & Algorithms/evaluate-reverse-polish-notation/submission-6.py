class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # valid operations are 
        # are we guarunteed its lawys valid?
        
        # to evaluate it
        # add number to a stack
        # when we find an operation: pop both values off the stack and apply the operation for them
        # after applying the operation append back onto the stack
        stack = []
        for val in tokens:
            if val.isnumeric() or len(val) > 1:
                # print(f"adding {val} to {stack}")
                stack.append(int(val))
            else:
                # print(f"found {val} with {stack}")
                # we know its an operation
                v1,v2 = stack.pop(), stack.pop()
                if val == "+":
                    stack.append(v1 + v2)
                elif val == "-":
                    stack.append(v2-v1)
                elif val == "*":
                    stack.append(v1 * v2)
                else:
                    value = v2/v1
                    if -0.5 < value < 0.5:
                        value = 0
                    else:
                        value = int(value)

                    stack.append(value)
        return stack[-1] # last value in the stack