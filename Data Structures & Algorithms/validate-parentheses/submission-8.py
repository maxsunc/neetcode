class Solution:
    def isValid(self, s: str) -> bool:
        # determine whether it iss a properly parentheses or not

        stack = []
        mapping = {"(":")","{":"}","[":"]"}

        # we need a way of getting the most recently opening
        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            else:
                if not stack:
                    return False
                # pop from the stack
                opening = stack.pop()
                if mapping[opening] != c:
                    return False
        # if we encounter open add to stack
        return len(stack) == 0

        # if we encunter closed (not open) take off the stack 