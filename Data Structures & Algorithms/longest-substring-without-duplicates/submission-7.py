class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length of the longest substring without duplcate characters

        # sliding window algorithm
        # dynamic sliding window:


        # zxyzxyz

        # keep a set of current characters in the substring

        # add characters to this substring,
        # if the character is within the set, remove from the set UNTIL that character no longer exists

        # o(n) time
        # o(n) space

        chars = set()

        l = 0
        res = 0

        for r in range(0, len(s)):
            # remove until the character no longer is in curChar
            curChar = s[r]
            while curChar in chars:
                # remove from the back
                chars.remove(s[l])
                l += 1
            
            # add the charaacter at r
            chars.add(curChar)
            res = max(res, r - l + 1)
        return res
        


