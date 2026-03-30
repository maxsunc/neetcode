class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permuation:
        # abc ==> cab, bac, bca, acb, abc 
        # lecabee 


        # str1, str2 ==> str1 = "cab", str2 = "abc"
        # hashmap

        # O(n * m) 

        if len(s2) < len(s1):
            return False

        # lceabee, abc

        # lecaabee
        s2Occurances = {}
        s1Occurances = {}
        # fill up the occurances for s1
        for c in s1:
            s1Occurances[c] = s1Occurances.get(c, 0) + 1
        

        # fill up our first len(s1) elements in charcterOccurance

        for i in range(len(s1)):
            s2Occurances[s2[i]] = s2Occurances.get(s2[i], 0) + 1
        
        if s2Occurances == s1Occurances:
            return True
        

        for i in range(len(s1), len(s2)):
            # lecabee, abc,, {"l" : 0}
            s2Occurances[s2[i]] = s2Occurances.get(s2[i], 0) + 1

            k = i - len(s1)
            s2Occurances[s2[k]] = s2Occurances.get(s2[k], 0) - 1
            if s2Occurances[s2[k]] <= 0:
                save_safe = s2Occurances.pop(s2[k], None)

            if s2Occurances == s1Occurances:
                return True







        return False








