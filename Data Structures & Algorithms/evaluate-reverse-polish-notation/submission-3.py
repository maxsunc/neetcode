class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1,2,+,3,*,4,- == > (1+2)*3
        # num, op
        stack = []
        result = 0
        for token in tokens:
            if token in "+-*/":
                a = (stack.pop())
                b = (stack.pop())
                print(token + str(b) + " " + str(a))
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(b-a)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
            else:
                # we get a number here
                # just add it to the stack
                stack.append(int(token))
        
        return stack.pop()

