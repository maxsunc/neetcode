class Solution:
    def isPalindrome(self, s: str) -> bool:
        # how do we check if its a valid palindrom?

        # cases dont matter

        # skip spaces

        # use two pointers to compare, converging


        l, r = 0, len(s)-1

        while r > l:
            # skip spaces for both
            while len(s) - 1 > l and (not s[l].isalnum()):
                l += 1
            while 0 < r and (not s[r].isalnum()):
                r -= 1
            if l > r:
                return True
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
