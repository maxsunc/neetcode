class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # take up to k replacements
        # find the length of the longest substring which only contains one distinct character.
        # O(26N) each iteration find the max freq elemetn in occurances in the window
        # 
        # 
        occurances = {}
        # greedy thought: we only need to track the highest frequency since if anything beats that frequency then we will say its worth our tijme, otherwise it isnt
        maxFreq = 0

        def getMostFreq():
            maxVal = 0
            for key in occurances:
                maxVal = max(maxVal, occurances[key])
            return maxVal

        res = 0
        left = 0

        for right in range(0, len(s)):
            occurances[s[right]] = occurances.get(s[right], 0) + 1
            maxFreq = max(maxFreq, occurances[s[right]])
            # one thing to detect for the O(N) solution: HOw do we find the most freq when we're reducing the size of the array?
            while (right - left + 1) - maxFreq > k:
                # we need to reduce the window size since itsx bigger than k
                occurances[s[left]] -= 1
                # no needs to update maxFreq
                left += 1
            
            # we know its valid
            res = max(res, right - left + 1)
            
        return res