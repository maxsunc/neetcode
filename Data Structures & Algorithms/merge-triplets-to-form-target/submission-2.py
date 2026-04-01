class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()

        for i in range(0, len(triplets)):
            triplet = triplets[i]
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue # if the vlaue ends up being larger it will neverb e usuable
            for i in range(0, 3):
                if target[i] == triplet[i] and not i in found:
                    found.add(i)
            # print(f"targets: {targetsMet}")
        # print(f"{foundTarget}")
        return len(found) == 3





        # 



