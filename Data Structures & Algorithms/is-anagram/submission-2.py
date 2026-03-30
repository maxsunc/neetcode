class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # definition of an anagram is same exact occurances
        oc1 = {}
        oc2 = {}

        for c in s:
            oc1[c] = oc1.get(c,0) + 1
        for c in t:
            oc2[c] = oc2.get(c,0) + 1
        
        return oc1 == oc2