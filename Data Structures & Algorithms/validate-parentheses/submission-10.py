class Solution:
    def isValid(self, s: str) -> bool:
        # we want to determine whether an input is a valid parenthesis:
        # openning must follow closed
        # closed bracket must correspond to open bracket of same type

        # is the input always valid? IOt only contains parentehsis right?

        # 1st approach: use a stack:
        # if its an openning parenthesis add it to a stack: the elements in the stack are all oppening
        # when its closing, pop from the stack and match, if it doesnt match return False
        # at the end if stack is still not empty we return false as well

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