class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # can ransomNote be made with leeter in magazine: is ransomNote a subset of magazine character

        # O(N + M) time and  O(26)

        occ1,occ2 = {}, {}
        for c in ransomNote:
            occ1[c] = occ1.get(c,0) + 1
        for c in magazine:
            occ2[c] = occ2.get(c,0) + 1
        
        for key in occ1:
            if occ2.get(key,0) < occ1[key]:
                return False
        return True