class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of the top k frequency elements

        # how do we do that?

        # the most frequent element can be seen at most n times

        # keep track of the occurances in a hashmap for each value

        # how do we organize it in a way that we can easily get the top k values in the hashmap?

        # max occurances is n

        # create an array of size n + 1, where n is the max number of occurances. the index at i = # occurances
        # foreach values found at an index, add to result and increment an index

        map = {}

        for num in nums:
            map[num] = map.get(num,0) + 1
        
        buckets = [[] for i in range(0, len(nums) + 1)]
        print('before')
        print(str(buckets))
        for key in map:
            numOccurances = map[key]
            print(str(buckets))
            buckets[numOccurances].append(key)

        res = [] 
        print(str(buckets))

        for i in range((len(buckets)-1), -1, -1):
            if len(buckets[i]) > 0:
                # elements exist here
                valsToAdd = buckets[i]
                for val in valsToAdd:
                    res.append(val)
                    if len(res) == k:
                        return res
        return res




