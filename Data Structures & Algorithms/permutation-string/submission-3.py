class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len(s1) <= len(s2) 
        # fit a window of size len(s1) into s2

        # def of permutation
        # abc => bac => cab 
        # occurance {a:1, b:1, c:1}
        occurances = {}
        # how do we check if occurances matches s1 occraucnes
        s1map = {}

        # build the s1 map
        for s in s1:
            s1map[s] = s1map.get(s,0) + 1

        k = len(s1)
        # check if occraucnes = s1map?
         

        # fixed sliding window
        for i in range(0, len(s2)):
            if i >= k:
                # remove s[i-k]
                occurances[s2[i-k]] = occurances.get(s2[i-k], 0) - 1

            occurances[s2[i]] = occurances.get(s2[i], 0) + 1
            isEqual = True
            # chekc if occruances matches the s1map
            for key in s1map:
                if s1map.get(key) != occurances.get(key,0):
                    isEqual = False
                    break

            if isEqual:
                return True
        return False

