class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Was it a car or a cat I saw?
        legend = set("abcdeqfghijklmnopqrstuvwxyz0123456789")


        l, r = 0, len(s)-1
        while r > l:
            while r > 0 and s[r].lower() not in legend:
                r -= 1
            while l < len(s) and s[l].lower() not in legend:
                l += 1
            if l >= len(s) or r < 0:
                return True
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        
        return True


