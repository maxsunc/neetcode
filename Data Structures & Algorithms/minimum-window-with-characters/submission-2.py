class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two string s and t fin the shortet substring of s such that every character in t is in that substring

        # sliding window
        # count the occurances: 

        # when the occurances end up matching t then reduce the size until it doesn't
        sOcc = {}
        tOcc = {}
        resLength = -1
        res = ""

        # count the occurances of t
        for c in t:
            tOcc[c] = tOcc.get(c,0) + 1
        def matches(h1,h2):
            # h1 is in h2
            for key in h1:
                if h1[key] > h2.get(key,0):
                    return False
            return True
        l = 0
        for r in range(0,len(s)):
            sOcc[s[r]] = sOcc.get(s[r],0) + 1
        # count the curOccurences we have
            while matches(tOcc,sOcc):
                print(f"matches for {s[l:r+1]}")
                # reduce the size
                sOcc[s[l]] -= 1
                
                if resLength == -1 or resLength > r - l + 1:
                    resLength = r - l + 1
                    res = s[l:r+1]
                l += 1

            
        
        return res


        # when the curOccurances satisfies the tOcc, reduce until that isnt the case

        # inbetween here save the min res