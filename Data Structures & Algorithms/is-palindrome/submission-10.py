class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ignore alphanumeric letters
        s = s.lower()
        # two pointer at both ends and iterate 
        l,r = 0, len(s) - 1

        while r >= l:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while 0 <= r and not s[r].isalnum():
                r -= 1
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
            


        return True