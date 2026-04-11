class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # def of an anagram is exaclty save occurances
        oc1 = {}
        oc2 = {}

        for c in s:
            oc1[c] = oc1.get(c,0) + 1
        
        for c in t:
            oc2[c] = oc2.get(c,0) + 1
        
        for key in oc1:
            if oc1[key] != oc2.get(key,0):
                return False
        for key in oc2:
            if oc2[key] != oc1.get(key,0):
                return False
            
        return True