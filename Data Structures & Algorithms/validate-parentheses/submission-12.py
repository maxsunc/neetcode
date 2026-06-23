class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = { "]" : "[", ")" : "(", "}" : "{" } # closing to openning
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                # we know its closing in this case, lets see if it matches
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0