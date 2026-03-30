class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # we want to get all the partitions 

        def isValid(checkStr):
            l, r = 0, len(checkStr) - 1
            while r > l:
                if checkStr[r] != checkStr[l]:
                    return False
                r -= 1
                l += 1
            return True

        res = []
        def backtrack(arr, curStr):
            if len(curStr) == 0:
                res.append(arr.copy())
                return
            
            checkStr = ""
            for i in range(0, len(curStr)):
                checkStr += curStr[i]
                # check if its a palindrom then we can go down that path
                if isValid(checkStr):
                    arr.append(checkStr)
                    backtrack(arr, curStr[i + 1:])
                    arr.pop() # remove the element to backtrack and try new possibilities 
        backtrack([],s)
        return res

            