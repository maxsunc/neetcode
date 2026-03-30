class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        # "zxyabc"
        # sliding window algoirthm
        left = 0
        maxLen = 1
        
        curChars = set()

        # 
        for right in range(0,len(s)):
            
            while(s[right] in curChars):
                # incremeent left 
                # get rid of character from left
                curChars.remove(s[left])
                left += 1
            curChars.add(s[right])
            maxLen = max(maxLen, (right-left+1))
            right += 1
        return maxLen
