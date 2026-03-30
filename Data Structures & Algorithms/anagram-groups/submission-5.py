class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def of an anagram is same exact occurances
        # separate it based on that 
        # there are only lowercase letters so we can use the buckets trick for 26 letters

        grouped = defaultdict(list) # key is tuple of size 26 

        # generate the key for each str
        for s in strs:
            buckets = [0] * 26
            for c in s:
                buckets[ord(c)-ord('a')] += 1
            grouped[tuple(buckets)].append(s)
        # put it in goruped


        # return the values
        return list(grouped.values())