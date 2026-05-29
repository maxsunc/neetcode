class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # definition of anagram => exactly same occurances

        # since its all just lowercase character

        # we want to group the anagrams together

        # in other words for each character find the occurances convert to tuple and put i into a map


        # return the values of that dictionary

        map = defaultdict(list)

        for s in strs:
            occ = [0 for i in range(0, 26)]
            for c in s:
                ind = ord(c)-ord('a')
                occ[ind] += 1
            
            # conver to tuple and check if its in map
            tupled = tuple(occ)
            map[tupled].append(s)
        
        return list(map.values())