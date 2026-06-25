class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find te longest substring that doesn't have repeating characters
        # edge cases:
        # returning the length fo the longest

        # brute force: check all subarrays: O(N^2)

        # sliding window + dictionary store the occurances of characters
        # zxyzxyz

        # keep track of the occurances of each character
        # have a left adn right pointers
        # whenever the occurance of a character is > 1: reduce the window size / remove elements from the window
        #  until that isnt the case O(N)

        occ = {}

        left = 0
        res = 0

        for right, c in enumerate(s):
            occ[c] = occ.get(c,0) + 1
            while occ.get(c,0) > 1:
                occ[s[left]] = occ.get(s[left],0) - 1
                left += 1
            # now we know this is valid
            res = max(res, right - left + 1)
        return res


        
