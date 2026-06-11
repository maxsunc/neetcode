class Solution:
    def decodeString(self, s: str) -> str:
        # return the decoded string of an encoded string
        # k[encoded_string)]
        # repeated k times

        # what qualifies something as a valid k value?
        # if its within a closing brackets then thats not good

        # 3[a2[bk]]2[bc]
        # curString = abkbkabkbkabkbkbcbc
        # curNum = 0
        # Numbers: [2]
        # characters: []


        # I think we should keep track of a stack
        # we're guarunteed that numbers follow a opening bracket
        # keep track of the lastSeenNumber as a string: 
        # when we get to closing brakcet we can deposit
        # when we get to an opening bracket deposit the curString
        # when we get to an ending bracket, pop from the stack to get the number to multiply the curString

        # have two stack: One for number and another for letters
        # when we get to a closing bracket: Pop from the stack of numbers and multiply to get curString
        # and then pop from the letter stack if its possible and add that to the front of curString
        # ['a']
        # [23,2]

        # 3[a]2[bc]

        curString, curNum = "", ""
        nums = []
        strings = []
        for c in s:
            if c.isnumeric():
                curNum += c
            elif c.isalpha():
                curString += c
            elif c == "[":
                # deposit curString and curNum and reset them
                nums.append(int(curNum))
                strings.append(curString)
                curString = ""
                curNum = ""
            elif c == "]":
                poppedStr = strings.pop()
                num = nums.pop()
                copy = curString
                # pop from the numbers and multiply the curString
                for i in range(1,num):
                    curString += copy
                # put in front the first value from strings
                curString = poppedStr + curString
        return curString

        