class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digits made up of digits from 2 to 9 inclusive
        # each digit
        # find all possible letter combinations that digits coujld represent

        # we may we return in any order

        # each number creates a different branch

        # we need to define what the values are from 2-9

        # backtracking problem
        map = {2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz"}


        # create a rcursive function

        # base case it will incremenet result or some global var

        # recursive case ( if its not at the end of digits) explore all possiblites
        res = []
        def backtrack(i, curStr):
            if i == len(digits):
                if len(curStr) != 0:
                    res.append(curStr)
                return
            s = int(digits[i])
            for c in map[s]:
            
                print(c)
                # curStr += c
                curStr += c
                backtrack(i + 1, curStr)
                # backtrack
                curStr = curStr[:-1]
        
        backtrack(0, "")
        return res
            
            

                