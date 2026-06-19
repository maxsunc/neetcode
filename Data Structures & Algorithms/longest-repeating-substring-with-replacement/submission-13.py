class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest repeating character with k replacements available

        # XYYX k = 2
        # AAABABB k = 1

        # we need some way to keep track of the currentMax freq
        # sliding window problem:
        # AAABABB k = 1
        # keep track of the current occurances
        # we also want to keep track of the maxOccurance
        

        # 1st: add it to an occurance, replace maxOccurance if needed
        # 2nd: check whether the size - maxOccurance > k which means we need k+ replacements
        # --> must reduce our window size
        # 3rd: we know this valid

        #  AAABABB

        # A : 1
        # B : 2

        # we want to find the length of the longest substring where we can replace up to k chracters and make all characters
        # identical
        # string s is uppercase english characters

        # if the windows needs more replacements tha k shrink the window from the left
        # keep track of the maximum length of such a window
        # AAABABB
        if not s:
            return 0

        # do the sliding window
        left = 0
        maxCount = 0
        counts = {} # occurances of each seen guy
        maxLength = 0

        for right in range(0, len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            maxCount = max(maxCount, counts[s[right]])

            while ((right - left + 1) - maxCount) > k:
                counts[s[left]] -= 1
                left += 1 # look at the next vlaue
            
            # we know its a valid window
            maxLength = max(maxLength, right - left + 1)
        return maxLength
            



