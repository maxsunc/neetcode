class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # find the minimium size of substirng that is within s that includes all characters of t
        if len(t) > len(s):
            return ""

        # is it guarunteed that len(t) <= len(s)
        # dynamic sliding window
        # 
        # is it guarunteed only lower and upper case?: in this case it owuld be O(62N) then
        tOcc = {}
        for index,c in enumerate(t):
            tOcc[c] = tOcc.get(c,0) + 1
        # print(tOcc)
        res = [-1,-1]
        resSize = math.inf
        l = 0
        sOcc = {}

        def subset(map1, map2):
            # find if map2 is a subset of map1
            for key in map2:
                if map1.get(key,0) < map2.get(key,0):
                    # print('flipo')
                    return False
            # passed the tests
            return True

        for r in range(0, len(s)):
            c = s[r]
            sOcc[c] = sOcc.get(c,0) + 1
            while subset(sOcc, tOcc):

                # capture as a result
                if r - l + 1 < resSize:
                    resSize = r - l + 1
                    
                    res = [l,r+1]
                    # print(s[res[0]:res[1]])
                

                # reduce it in size
                sOcc[s[l]] -= 1
                l += 1
            
        return s[res[0]:res[1]] 