class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False
        hash_map = {}
        hash_map["("] = ")"
        hash_map["["] = "]"
        hash_map["{"] = "}"
        expected = []
        for c in s:
            if(c in hash_map):
                expected.append(hash_map[c])
            else:
                if len(expected) == 0:
                    return False
                val = expected.pop()
                if val != c:
                    return False
        if(len(expected) != 0):
            return False
        
        return True

            