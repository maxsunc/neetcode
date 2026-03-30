class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ")"
        # "(())"

        # can only add open if numClosed == open
        # we can add open or closed if numClosed < numOpen and numOpen < n (()(

        
        res = []
        # n = 1
        # 
        def buildParenthesis(numOpen, numClosed, currentParenthesis):
            if numOpen == n and numClosed == n:
                res.append(currentParenthesis)
                return
            print(f'{numOpen} + {numClosed}')

            # check if we can add an open
            if numClosed == numOpen:
                print('they equal')
                currentParenthesis += "("
                buildParenthesis(numOpen + 1, numClosed, currentParenthesis)
                return

            # (numClosed < numOpen and numOpen < n)
            if (numClosed < numOpen and numOpen < n):
                buildParenthesis(numOpen + 1, numClosed, currentParenthesis +"(")
                buildParenthesis(numOpen, numClosed + 1, currentParenthesis +")")
                return
            else:
                print('hello')
                buildParenthesis(numOpen, numClosed + 1, currentParenthesis +")")
                return
        
        buildParenthesis(0,0,"")
        return res





            





            

        