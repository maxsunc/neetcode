class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the k mot frequent elemnts

        # what if we used a heap :thinking_emoji:

        # keep track of the occurances of each element n + nlogk
        occurances = {}
        # heap = []

        for n in nums:
            occurances[n] = occurances.get(n,0) + 1
        
        # # add each element to the heap
        # for key in occurances:
        #     entry = (-occurances[key], key)
        #     heapq.heappush(heap, entry)

        # res = []
        # # take the top k elements from the heap
        # for i in range(0, k):
        #     entry = heapq.heappop(heap)
        #     res.append(entry[1])
        # return res

        # sol 2: O(n) solution:
        res = []

        buckets = [[] for i in range(0, len(nums) + 1) ] 

        # using occurances place the value in the correct bucket
        for key in occurances:
            numOcc = occurances[key]
            buckets[numOcc].append(key)
        counter = 0
        for i in range(len(nums), -1, -1):
            arr = buckets[i]
            for val in arr:
                res.append(val)
                counter += 1
                if counter >= k:
                    return res
        return res


        
        # soln 1: order by heap (occurance, elemnt)

        # take the top k elements

        # O(n) time how do we get this?


        # weird thought but the number of occurances can only be as high of the length of the array (n) so all we need to do
        # is use a List of Lists instead of a hashmap
        # then just traverse it in the backwards order 
        