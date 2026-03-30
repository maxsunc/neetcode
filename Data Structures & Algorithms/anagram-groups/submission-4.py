class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["act","pots","tops","cat","stop","hat"]
        # definiton of an anagram is same exact occurances of characters
        # 
        # how do we catagorize occurances?
        # use a buckets as a key (tuple of length 26)
        # the value is a list of strings
        myDict = defaultdict(list)

        for s in strs:

            # count occurences and store as a tuple
            occurances = [0] * 26
            for c in s:
                occurances[(ord(c) - ord('a'))] += 1
            
            # check if our occcurances is within our dictionary
            myDict[tuple(occurances)].append(s)
        return list(myDict.values())

            

        
    

