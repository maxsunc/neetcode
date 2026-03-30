class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # def of an anagram = same occurances exactly
        sOcc = {}
        tOcc = {}

        for c in s:
            sOcc[c] = sOcc.get(c,0) + 1
        for c in t:
            tOcc[c] = tOcc.get(c,0) + 1
        
        return tOcc == sOcc
