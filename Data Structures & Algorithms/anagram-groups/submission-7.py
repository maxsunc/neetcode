class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def of an anagram is occurances of character
        # since they're all just lowercase letters we can store a tuple of size 26
        hashed = defaultdict(list)
        for s in strs:
            # create the tuple
            occ = [0 for j in range(0, 26)]
            for c in s:
                ind = ord(c)- ord('a')
                occ[ind] += 1
            # convert to tuple and hash
            tupled = tuple(occ)
            hashed[tupled].append(s)
        
        return list(hashed.values())