class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundTarget = [False for i in range(0,3)]

        for i in range(0, len(triplets)):
            triplet = triplets[i]
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue # if the vlaue ends up being larger it will neverb e usuable
            for i in range(0, 3):
                if target[i] == triplet[i]:
                    foundTarget[i] = True
            # print(f"targets: {targetsMet}")
        # print(f"{foundTarget}")
        for i in range(0,3):
            if not foundTarget[i]:
                return False
        return True





        # 



