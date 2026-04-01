class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # [1,3,1]
        # [2,1,2] 
        # => [2,3,2]
        # return True if its possible to obtain target

        # [[1,2,3],[7,1,1]]  ==> [7,2,3]
        # [7,2,3]

        # max(a[i],a[j]), max(b[i],b[j]), max(c[i],c[j])

        
        
        # backtracking problem: Try all different scenrios 
        # n^n solution
        # bring it down with memoization: cache the triplet result as false or true
        # merge t1 with t2 this is the same as merging t2 with t1
        # the order in which you merge it also matters

        # that is too slow 

        # [[1,2,3],[7,1,1]]
        # [7,2,3]

        # triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]

        # [5,7,5]
        
        # foreach of the triplets with values we need
        # we should check whether the other values are < the target vlaues as well

        # for example for [2,5,6] this has 6 that we want
        # in index 0: 2 < 5: GOOD
        # in index 1: 5 > 4: BAD (we can't transform into 4 anymore)

        # keep track of the seen target values as a array of size 3
        # we only set the seen target value to true
        # if the target is seen at that position AND all other non related values indicies
        # are less than target values
        foundTarget = [False for i in range(0,3)]

        for i in range(0, len(triplets)):
            targetsMet = [False for i in range(0,3)]
            triplet = triplets[i]
            validTriplet = True
            for i in range(0, 3):
                if target[i] < triplet[i]:
                    validTriplet = False
                    break
                elif target[i] == triplet[i]:
                    targetsMet[i] = True
            if not validTriplet:
                print("not valid contining")
                continue
            # print(f"targets: {targetsMet}")
            
            for i in range(0,3):
                if not foundTarget[i]:
                    foundTarget[i] = targetsMet[i]
        # print(f"{foundTarget}")
        for i in range(0,3):
            if not foundTarget[i]:
                return False
        return True





        # 



