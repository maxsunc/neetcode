class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # return unique combinations of candidates where the numbers equal sum

        # sort the candidates?
        # chosen numbers sum to target
        # cant use duplicates?
        # brute force
        # mySet = set()
        candidates.sort()
        # each character is either take or not take?
        res = []
        # why do we need to sort this?
        def backtrack(index, curSum, comb):
        # base cases
            if curSum == target:
                # if tuple(comb) in mySet:
                #     return
                # mySet.add(tuple(comb))
                res.append(comb.copy())
                return
            if index == len(candidates):
                return
            # case 1: take the element (and look at next)
            newComb = comb.copy()
            newComb.append(candidates[index])
            backtrack(index + 1, curSum + candidates[index], newComb)
            # skip duplicate elements
            duplicate = candidates[index]
            newIndex = index
            while newIndex < len(candidates) and duplicate == candidates[newIndex]:
                newIndex += 1
            # case 2: dont take the element (and look at next)
            backtrack(newIndex, curSum, comb)
        backtrack(0, 0, [])
        
        return res