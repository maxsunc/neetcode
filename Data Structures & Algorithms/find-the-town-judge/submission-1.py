class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # n people
        # array of trusts
        # 1 --> 3
        # 4 -- > 3
        # 2 --> 3
        # town judge doesnt trust anyone
        # 

        # 1--> 3
        # 2-->3
        # 3-->1
        #3-->2
        
        # hashmap

        # hashmap with int value and array of people you trust and another array of people who trust you
        #

        # 4-->1
        # 1-->2
        # 2-->1
        # 1-->3
        # 4-->2
        map = {}
        map2 = {}
        for i in range(1, n + 1):
            map[i] = []
            map2[i] = []
        # build that hashmap 
        for t in trust:
            val1 = t[0]
            val2 = t[1]
            
            map[val1].append(val2)
            map2[val2].append(val1)
        

        # look for person with 1. trusting no one 2. everyone trusts you
        for key in map:
            if len(map[key]) == 0 and len(map2[key]) == n - 1:
                return key
        return -1
        


