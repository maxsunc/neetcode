class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def inBounds(i):
            return 0 <= i < len(s)

        
        def sol(i):
            nonlocal res
            if i == len(s):
                return
            # 1: for each elemnt try to extend outward
            l, r = i-1, i + 1
            res += 1
            while inBounds(l) and inBounds(r):
                if s[l] != s[r]:
                    break
                # s[l] == s[r] so lets update res
                # updateRes(l,r)
                # aba
                res += 1
                l -= 1
                r += 1
            # check if we can go in the even
            if inBounds(i+1) and s[i+1] == s[i]:
                l,r = i, i + 1
                while inBounds(l) and inBounds(r):
                    if s[l] != s[r]:
                        break
                    # s[l] == s[r] so lets update res
                    # updateRes(l, r)
                    res += 1
                    # aba
                    l -= 1
                    r += 1
            
            sol(i+1)
        
        sol(0)
        return res
            
