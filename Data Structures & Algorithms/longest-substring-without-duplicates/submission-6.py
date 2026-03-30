class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substirng without duplicate characters

        # dynamic sldiing window 

        # keep track of already seen values
        seen = set()
        res = 0

        # left and right pointer
        left = 0
        # right pointer 

        for right in range(0, len(s)):
        # while a value on the right is already in the set remove from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res
            

