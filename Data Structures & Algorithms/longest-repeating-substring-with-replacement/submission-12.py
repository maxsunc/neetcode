class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        # idea: Dynamic sliding window

        # whenever there are no more replacements left  ake away from the left until there are some more
        # Always have to recalculate the most Frequent element

        l = 0
        res = 0

        for r in range(0, len(s)):
            # add the encountered elements to our cur freq
            freq[s[r]] = freq.get(s[r],0) + 1

            # check if we have enough replacmeents
            mostFreq = max(freq.values())
            replacementsNeeded = r-l + 1 - mostFreq
            while replacementsNeeded > k:
                # reduce from here and recualculate teh most Freq
                freq[s[l]] = freq.get(s[l],0) - 1
                l += 1
                mostFreq = max(freq.values())
                replacementsNeeded = r-l + 1 - mostFreq
            res = max(res, r-l+1)

        return res
            