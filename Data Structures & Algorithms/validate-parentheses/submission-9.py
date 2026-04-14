class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"{":"}","[":"]","(":")"}

        # add to stack if its opening
        # if its closing pop from stack
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                # closing bracket
                if not stack:
                    return False
                top = stack.pop()
                if c != match[top]:
                    return False
        return len(stack) == 0
