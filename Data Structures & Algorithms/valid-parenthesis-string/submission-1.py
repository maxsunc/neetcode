class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, starStack = [], []

        for i,c in enumerate(s):
            if c == "(":
                stack.append(i) # keep track of the index so at the end if we have too many open
                # use some star with index > bracketIndex to cover
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    # we have an empty stack, use a star stack reserve
                    if starStack:
                        # indexOpening = stack[-1]
                        # indexStar = starStack[-1]
                        starStack.pop()
                    else:
                        return False # nobody can save you
            else:
                starStack.append(i)   
        print(f"remaining: {stack}")
        print(f"star: {starStack}")
        while stack:
            print(stack)
            # stack is still looking for values
            if starStack and starStack[-1] > stack[-1]:
                stack.pop()
                starStack.pop()
            else:
                return False
        return True


