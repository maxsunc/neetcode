class Solution:
    def longestPalindrome(self, s: str) -> str:
        # find the longest palindrome in s

        # definition of a palin drome: Reads the same forward and backward


        # two pointers:
        # ababd

        # longest substring s that is a palindrom

        # ababd

        # for each element within s, 
        # check if we can extend out to form a palindrom
        # check if at i + 1 is the same element then check if we can extend out from i and i + 1 as well
        # 
        res = 1
        left, right = 0,0
        def inBounds(i):
            return 0 <= i < len(s)
        def updateRes(l,r):
            nonlocal res
            nonlocal left
            nonlocal right
            if (r - l + 1) > res:
                res = r - l + 1
                left = l
                right = r
                print(f"new result {s[left:right+1]}")

        
        def sol(i):
            nonlocal res
            if i == len(s):
                return
            # 1: for each elemnt try to extend outward
            l, r = i-1, i + 1
            while inBounds(l) and inBounds(r):
                if s[l] != s[r]:
                    break
                # s[l] == s[r] so lets update res
                updateRes(l,r)
                # aba
                l -= 1
                r += 1
            # check if we can go in the even
            if inBounds(i+1) and s[i+1] == s[i]:
                l,r = i, i + 1
                while inBounds(l) and inBounds(r):
                    if s[l] != s[r]:
                        break
                    # s[l] == s[r] so lets update res
                    updateRes(l, r)
                    # aba
                    l -= 1
                    r += 1
            
            sol(i+1)
        
        sol(0)
        return s[left:right + 1]
            
