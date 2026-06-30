class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # take up to k replacements
        # find the length of the longest substring which only contains one distinct character.
        # O(26N) each iteration find the max freq elemetn in occurances in the window
        # 
        # 
        occurances = {}
        def getMostFreq():
            # return the highest frequency
            if not occurances:
                return 0
            maxVal = 0
            for key in occurances:
                maxVal = max(maxVal, occurances[key])
            return maxVal

        res = 0
        left = 0

        for right in range(0, len(s)):
            occurances[s[right]] = occurances.get(s[right], 0) + 1
            # one thing to detect for the O(N) solution: HOw do we find the most freq when we're reducing the size of the array?
            while (right - left + 1) - getMostFreq() > k:
                # we need to reduce the window size since itsx bigger than k
                occurances[s[left]] -= 1
                left += 1
            
            # we know its valid
            res = max(res, right - left + 1)
            
        return res