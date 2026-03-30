class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 2 to 9 inclusive
        # get all combinations of a phone number

        # define what each number represents
        map = {2 :"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

        # take in curStr and seq
        res = []
        def backtrack(seq, curStr):
            if len(seq) == 0:
                if curStr:
                    res.append(curStr)
                return
            
            # for each of the letters explore the possibilities
            curChar = seq[0]
            seq = seq[1:]
            # print(int(curChar ))
            s = map[int(curChar)]
            for c in s:
                oldStr = curStr
                curStr += c
                backtrack(seq, curStr)
                # backtracking step to explore other possibilities
                curStr = oldStr
        backtrack(digits,"")
        return res



        