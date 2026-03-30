class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Find whether s2 contains a permutation of s1 
        # if that is the case return True
        # otehr wise false

        # definition of a permutation: same exact occurances of elements with the same length 

        # O(26n) solution: 

        # fixed sliding window of length s1
        # 
        s1Occur = {}
        for i in range(0, len(s1)):
            s1Occur[s1[i]] = s1Occur.get(s1[i], 0) + 1
        print(s1Occur)
        l = 0
        s2Occur = {}

        for r in range(0, len(s2)):
            
        # Stage one filling in the window with occurances
            s2Occur[s2[r]] = s2Occur.get(s2[r], 0) + 1
            print(f"checking {l} {r} {s2Occur}")
            if r - l + 1 == len(s1):
        # check occurances match    
                match = True
                for key in s2Occur:
                    if s2Occur[key] == 0:
                        continue
                    if key not in s1Occur:
                        match = False
                        break
                    if s1Occur.get(key,0) != s2Occur[key]:
                        match = False
                        break
                if match:
                    return True
                # remove the last element since we'll add another one soon
                s2Occur[s2[l]] -= 1
                l += 1
        return False




        # remove the last element when we're full
