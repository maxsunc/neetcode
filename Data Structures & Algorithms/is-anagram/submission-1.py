class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        # lengths are the same here
        map1 = {}
        map2 = {}

        # if the lengths aren't the same
        # return false

        for i in range(0,len(s)):
            map1[s[i]] = map1.get(s[i], 0) + 1
            map2[t[i]] = map2.get(t[i], 0) + 1
        
        for key in map1:
            if(map2.get(key,0 ) != map1.get(key,0)):
                return False
        
        return True
            