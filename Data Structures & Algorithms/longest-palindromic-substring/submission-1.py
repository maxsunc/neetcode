class Solution:
    def longestPalindrome(self, s: str) -> str:
        # find the longest substring of s that is a palindrome
        # two pointer approach O(n^2)
        # plaindrome could be odd or even legnth
        # for each string extend outward
        # O(n^2) approach so for each of them try extending outwards
        if len(s) == 0:
            return 0
        
        res = s[0]
        resLength = 1

        for i,c in enumerate(s):
            # try for odd length first
            l,r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLength:
                    resLength = r - l + 1
                    print(f"updating res to {l} to {r}")
                    res = s[l:r+1]
                l -= 1
                r += 1
            # try for even length only if the next elmeent is the same
            if i + 1 >= len(s) or s[i+1] != s[i]:
                continue
            if resLength < 2:
                resLength = 2
                res = s[i:i + 2]
            l,r = i - 1, i + 2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if r - l + 1 > resLength:
                    resLength = r - l + 1
                    print(f"updating res to {l} to {r}")
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res
            
                

