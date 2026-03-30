class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 2 strings s t
        # find shortest substring of s so every character of t is in that substring

        # but we want the minimum
        # Only consist of english characters => O(26n) = O(n)


        # extend window until we have same characters as t

        # if we have the same characters as t already then reduce the window until we dont have the same characters as t
        # 
        tOcc = {}

        for c in t:
            tOcc[c] = tOcc.get(c, 0) + 1

        def overlap(occ1, occ2): # occ2 is smaller than occ 1
            # returns whether occ2 overlaps with occ1
            for key in occ2:
                if occ1.get(key, 0) < occ2.get(key, 0):
                    return False
            
            return True


        print(f"tocc: {tOcc}")
        l = 0
        sOcc = {}
        resLength = len(s) + 1
        res = ""

        for r in range(0, len(s)):
            # always add it in no matter waht
            sOcc[s[r]] = sOcc.get(s[r], 0) + 1
            # check if we match the occurances
            print(f"{sOcc} with {overlap(sOcc,tOcc)}")
            while overlap(sOcc, tOcc):
                
                if r-l+1 < resLength:
                    resLength = r-l+1
                    res = s[l:r + 1]

                # reduce sOcc until no more overlap
                sOcc[s[l]] -= 1
                print(sOcc)
                l += 1
        
        # print(resLength)
        return res

        





