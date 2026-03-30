class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # act, cat 
        # set() {a}
        # have anagram hashmap
        # 
        res = {} # tuple, list

        for s in strs:
            bucket = [0] * 26
            for c in s:
                ind = ord(c) - ord('a')
                bucket[ind] += 1
            key = tuple(bucket)
            if key not in res:
                res[key] = []
            res[key].append(s)

        
        return list(res.values())

            

        
    

