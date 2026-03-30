class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}  # <str, int>
        # max size of seen is 26 O(26n)
        left = 0
        result = 0
        maxFreq = 0

        for right in range(0, len(s)):
            # add it to dictionary
            seen[s[right]] = seen.get(s[right],0) + 1
            
            maxFreq = max(maxFreq, seen[s[right]])

            curLen = right - left + 1
            if curLen - maxFreq > k:
                curLen-=1
                # shift up left
                seen[s[left]] -= 1
                left += 1 
                # AAABC
                
            result = max(curLen, result)

        return result





