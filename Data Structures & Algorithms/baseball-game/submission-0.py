class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for s in operations:
            if s in "+DC":
                if s == "C":
                    stack.pop()
                elif s == "D":
                    val1 = stack[len(stack)-1]
                    stack.append(val1*2)
                elif s == "+":
                    val1 = stack[len(stack)-1]
                    val2 = stack[len(stack)-2]
                    stack.append(val1+val2)
            else:
                stack.append(int(s))
        return sum(stack)