class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of the longest length in res or something

        # without repeating characters => using a set
        # everytime we encounter a repeated element, remove the leftmost value
        l = 0
        curSet = set()
        r = 0
        res = 0
        while len(s) > r:
            while s[r] in curSet:
                # remove value from left and incremenet left
                curSet.remove(s[l])
                l += 1
            
            # add the value at r
            curSet.add(s[r])

            res = max(r - l + 1, res)
            r += 1
        return res
