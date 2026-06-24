class Solution:
    def isPalindrome(self, s: str) -> bool:

        # simple: is it a palindrome? Skip all none alpha numeric and bring to lowercase

        # two pointers that converge
        # skip the pointers along while they aren't alphanumeric characters
        # "Was it a car or a cat I saw?"
        # when the pointers cross return True
        # if the pointers at alphanumeric dont match then return false

        l, r = 0, len(s) - 1

        while r > l:
            # skip all alphanumeric characters
            while r > l and not s[r].isalnum() :
                r -= 1
            while r  > l and not s[l].isalnum():
                l += 1
            if l >= r:
                return True
            # they're alnum characters now
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True