class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the k most frequent elements within an array
        # O(N) solution is 

        # track the frequencies of each 

        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        # the frequency of an element can never exceed the length of nums
        buckets = [[] for i in range(0, len(nums) + 1)]

        for key,val in freq.items():
            buckets[val].append(key)
        
        res = []

        for i in range(len(nums), -1, -1):
            for j in range(0, len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
        return res