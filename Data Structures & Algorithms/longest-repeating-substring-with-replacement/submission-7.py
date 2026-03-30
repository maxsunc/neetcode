class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # XYYX
        # xxxx
        # yyyy


        # AAABABBBBB
        # AAAAABB
        # AAABBBB

        # use two pointers to represent window start and end
        # keep trakc of frequencies of each character inside the window
        # keep track of max freq we find = our main element
        # how do we updat ethis frequency?
        # if numNonMainChars > k
        # increase let pointer until we get to window that works
        # how do we update maxFreq in this case?
        seen = {}
        l = 0
        res = 0

        for r in range(0, len(s)):
            # update the freqency
            seen[s[r]] = seen.get(s[r], 0) + 1
            # update max freq
            maxFreq = 0
            for val in seen.values():
                maxFreq = max(val, maxFreq)

            # check if nonMainChars > k
            numNonMainElements = (r-l+1) - maxFreq
            while (numNonMainElements) > k:

                # exceeded threshold value, mush reduce!
                seen[s[l]] = seen.get(s[l], 0) - 1
                print("removing " + str(s[l]))
                l += 1
                # re calc max freq:
                maxFreq = 0
                for val in seen.values():
                    maxFreq = max(val, maxFreq)
                numNonMainElements = (r-l+1) - maxFreq
            res = max(res, r-l+1)

        return res








