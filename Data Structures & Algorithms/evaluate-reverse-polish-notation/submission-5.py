class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # reverse polish notation: 
        # keep track of the numbers in a stack
        # whenever operation comes in apply the operation between the two numbers

        # [1,2]
        # [3]
        # [3,3]
        # [9]
        # [9,4]
        # [5]
        # always valid

        stack = []

        for i in range(0, len(tokens)):
            val = tokens[i]
            if val in "+-/*":
                
                # its an operation so apply the correct operation
                v1 = stack.pop()
                v2 = stack.pop()
                print(f"Operation {v2}{val}{v1}")
                newVal = 0
                if val == "+":
                    newVal = v1 + v2
                elif val == "-":
                    newVal = v2 - v1
                elif val == "*":
                    newVal = v2 * v1
                else:
                    newVal = v2 / v1
                    if newVal > 0:
                        newVal = math.floor(newVal)
                    else:
                        newVal = math.ceil(newVal)
                stack.append(newVal)
            else:
                print(val)
                stack.append(int(val))
        
        # the stack wshould just have one element now
        return stack[-1]
                    
