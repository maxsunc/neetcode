class Solution:
    def decodeString(self, s: str) -> str:
        # assuming it is always valid

        # 2[string to repeat]

        # 2[a3[b]]c
        
        # 10[abc]

        # store the number somewhere 
        # [] have to do with the stack (I think )

        # look at the opening [ brackets and clos

        # iterate, everytime we encounter a number add it to the curNumber and curString

        # everytime we encounter a letter add to curString and clear curNumber


        # 2[a3[b2[c]]]c
        # 

        # everytime we see a number expect a [ next
        # assuming its always valid we can just append to number if its a number, str if its a str
        # 
        res = ""
        curStr = ""
        curNum = ""
        # a2[a3[b]]c
        # 
        stack = []

        # stack contains tuple (number, content)
        # when you encounter a [ add to the sgtack
        for c in s:
            if c.isnumeric():
                curNum += c
            elif c == "[":
                # reset the curString and add to res (if stack is empty)
                if not stack:
                    res += curStr
                else:
                    stack[-1][1] += curStr
                # if stack is NOT empty that means we want to add a new multiple within another multiple
                # add curStr to top of stack's element
                # now we're making a new bracket with curNum multiplier
                entry = [int(curNum), ""]
                stack.append(entry)
                # reset curStr since we're looking at a new. bracket
                curStr = ""
                curNum = ""
            elif c == "]":
                print(stack)
                # do some other stuff
                # close the bracket (add to result OR top of stack)

                # pop from stack
                entry = stack.pop()

                # add our curStr to entry
                entry[1] += curStr

                # generate the full str of the multiplier
                fullStr = int(entry[0]) * entry[1]
                # add to res if not stack
                if not stack:
                    res += fullStr
                else:
                    stack[-1][1] += fullStr
                curStr = ""
                
            else:
                # its a alphabet character
                curStr += c
        res += curStr
        
        return res





