class Solution:
    def simplifyPath(self, path: str) -> str:
        # always begins with a slash
        # . = current (nothing)
        # .. = go back

        # ... = actual directory
        # consequtivty slash = /

        # iterate through the string

        # using a stack we want to filter out useless stuff
        # add a slash when we see it 
        # if the top of the stack is a slash dont add that slash we're looking at

        # track the current word by just adding it to a string and when we encounter a slash add 
        # that current word to the stack
        # we cna also check if its .. or a . ( . => skip dont add to stack)

        stack = []
        curStr = ""

        for c in path:
            if c == "/":
                print(curStr)
                # add the current str to the stqack if its not empty or a period/..
                if len(curStr) != 0:
                    if curStr == '..':
                        if len(stack) > 0:
                            print("popping " + stack[-1])
                            # reduce the stack size  if not already small
                            stack.pop()
                    elif curStr != ".":
                        # add this path to the staack
                        stack.append(curStr)


                # reset curStr
                curStr = ""
            else:
                curStr += c

        if len(curStr) != 0:
            if len(curStr) != 0:
                if curStr == '..':
                    if len(stack) > 0:
                        print("popping " + stack[-1])
                        # reduce the stack size  if not already small
                        stack.pop()
                elif curStr != ".":
                    # add this path to the staack
                    stack.append(curStr)
        
        # build the result iwth stack
        res = ""
        for s in stack:
            res += "/"
            res += s
        if len(res) == 0:
            res += "/"
        # 
        return res