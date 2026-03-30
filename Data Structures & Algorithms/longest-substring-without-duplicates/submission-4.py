class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        curSet = set()
        res = 0
        for right in range(0, len(s)):
            while s[right] in curSet:
                # remove left guy
                curSet.remove(s[left])
                left += 1
            curSet.add(s[right])
            res = max(res, right - left + 1)

        return res