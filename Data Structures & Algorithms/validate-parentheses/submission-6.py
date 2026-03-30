class Solution:
    def isValid(self, s: str) -> bool:
        # append to the stack if it is an openning brackt
        stack = []
        mapping = {"}": "{", ")" : "(", "]":"["}
        
        # if it is a closing bracket to get the most recent openning bracket just take off from the stack
        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            else:
                # we know iti s a closing bracket since it only consists of brackets
                if not stack:
                    return False
                opening = stack.pop()
                if mapping[c] != opening:
                    return False
        return len(stack) == 0
