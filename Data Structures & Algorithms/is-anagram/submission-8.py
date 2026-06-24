class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap problem
        # occurances must match
        if len(s) != len(t):
            return False
        o1,o2 = {}, {}

        for c in s:
            o1[c] = o1.get(c,0) + 1
        for c in t:
            o2[c] = o2.get(c,0) + 1
        
        for key in o1:
            if o1.get(key, 0) != o2.get(key,0):
                return False
        return True