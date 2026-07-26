class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # find all well-formed parentheses strings that you can generate with n pairs of parenthesis

        # n=1
        # ()
        
        # n=2
        # (())
        # ()()

        # find all cases: backtracking
        res = []

        # keep track of the current open and closing parenthesis left
        def backtrack(openingLeft, closingLeft, s):
            # print(f"{openingLeft} closing: {closingLeft}")
            if openingLeft == 0 and closingLeft == 0:
                res.append(s)
                return
            
            if openingLeft > 0:
                s += "("
                backtrack(openingLeft - 1, closingLeft,s)
                s = s[:-1] # backtracking
            if closingLeft > 0 and openingLeft < closingLeft:
                s += ")"
                backtrack(openingLeft, closingLeft - 1, s)
                s = s[:-1]

        backtrack(n,n,"")
        return res                
                
