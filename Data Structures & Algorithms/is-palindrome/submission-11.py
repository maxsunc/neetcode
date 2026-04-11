class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filtero ut all alphanum charas and just compare the reversed 
        # O(n) time , O (n) extra space
        filter = ""
        for c in s:
            if c.isalnum():
                filter += c.lower()
        
        return filter == filter[::-1]
