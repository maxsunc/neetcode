class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappaHash = {} # [List[str], List<str>]

        #[26] [1,0,0,1,000,1,0000..0]
        for s in strs:
            # create a new list with bucket of values
            bucket = [0] * 26
            for c in s:
                bucket[ord(c) - ord('a')] += 1
            
            # convert bucket to a string!
            key = "#".join(str(x) for x in bucket)
            
            # check if the bucket exists in the mappahash
            if(key in mappaHash):
                mappaHash[key].append(s)
            else:
                newList = [s]
                # doesn't exist so make a new one!
                mappaHash[key] = newList
        # result
        result = []
        for val in mappaHash:
            result.append(mappaHash[val])

        return result