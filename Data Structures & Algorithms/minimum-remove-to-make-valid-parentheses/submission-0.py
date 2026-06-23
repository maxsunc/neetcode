class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # find the minimium number of removals needed to make the string valid
        # return the valid string

        # is it possible to make a string valid in multiple ways?

        # ()
        # only thing we're looking at is this paraenthesises.

        # "nee(t(c)o)de)"
        # "nee(t(c)ode)"
        # 
        # we can return any of the ways to make it valid

        # stack?: add opening parenthesis to this stack and pop from it when we 
        # find a closing parentehsis
        # string.remove? 
        # generate a new result string
        

        # when we find a closing parenthesis while we have no open: just dont add it
        # (()
        # two cases of invalid:
        # too many closing:
        # --> Dont add it to the result string
        # too many opening
        # --> 


        # "nee(t(c)ode"

        # instead of immediantly adding to resultWord
        # resStack = [] # store everything, recomposed at the end:
        # store elements with (element, index)
        # stack = [] 
        # bannedIndex = set()

        # [("(", index)]
        # at the end: we have toomany opening:
        # pop from stack and add to bannedIndex


        # we wanna build the result with resStack:
        # keep popping until empty
        # add to result if not banned

        # "))()(("

        # TimeComplexity: O(N), space: O(N)
        stack, resStack = [], deque()
        bannedIndexes = set()

        for i, c in enumerate(s):
            element = (c, i)
            if c == "(":
                # add to stack and res stack
                stack.append(element)
            elif c == ")":
                # try to pop, if we can dont ban it, if we cant pop it. Then ban it
                if stack:
                    stack.pop()
                else:
                    bannedIndexes.add(i)
            resStack.append(element)
        # ban remaining opening parenthesis
        while stack:
            element = stack.pop()
            bannedIndexes.add(element[1])
        # build the result
        result = ""
        while resStack:
            element = resStack.popleft()
            if element[1] not in bannedIndexes:
                result += element[0]
        return result


