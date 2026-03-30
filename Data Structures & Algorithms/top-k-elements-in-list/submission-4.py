class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}

        for i in nums:
            map1[i] = map1.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for i in map1.keys():
            (buckets[map1.get(i)]).append(i)
            print(map1.get(i))
        res = []
        counter = 0

        for i in range(len(nums), -1, -1):
            
            if(len(buckets[i]) != 0):
                print("looking at " + str(i) + " with length " + str(len(buckets[i])))
                # we have elements here
                bucket = buckets[i]
                for j in bucket:
                    res.append(j)
                    counter += 1
                    if counter == k:
                        return res


        return res
