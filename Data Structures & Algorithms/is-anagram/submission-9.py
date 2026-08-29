class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return True if it is an anagram, false if not
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}

        for c in s:
            map1[c] = map1.get(c,0) + 1
        for c in t:
            map2[c] = map2.get(c,0) + 1
        for key in map1:
            if map2.get(key,0) != map1[key]:
                return False
        return True
