class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the k most frequent integers that appear most frequently
        
        # [1,2,2,3,3,3]
        # 
        # group the numbers by occurances

        # 1. Get the occurances of each character
        occ = {}
        # group my occurances
        for num in nums:
            occ[num] = occ.get(num, 0) + 1
        # iterate from above down 
        grouped = [[] for i in range(0, len(nums) + 1)]
        for key in occ:
            val = occ[key]
            grouped[val].append(key)
        
        res = []

        for i in range(len(grouped) - 1, -1, -1):
            arr = grouped[i]
            print(arr)
            for j in range(0, len(arr)):
                res.append(arr[j])
                if len(res) == k:
                    return res
        return res



        # 