class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if len(s) == 0:
            return 0
        # dynamic sliding window problem
        # set data structue for each new potential substring
        # 
        values = set()

        # xzyzebc
        maxLen = 1
        curLen = 1
        values.add(s[0])
        # {x}
        for i in range(1, len(s)):
            if s[i] in values:
                # problem
                # decrease our len and remove the lement at i - curLen
                while s[i] in values:
                    # remove the last guy
                    if s[i-curLen] in values:
                        values.remove(s[i-curLen])
                    curLen -= 1
            values.add(s[i])
            curLen += 1
            maxLen = max(maxLen, curLen)


        return maxLen

