class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for c in s:
            freq[c] = freq.get(c,0) + 1
        # put the highet frequency stuff first before rthe lowest frequency
        maxHeap = []
        # entries will be (freq, c)
        for key in freq:
            entry = (freq[key] * -1, key)
            heapq.heappush(maxHeap, entry)
        

        res = ""
        # wait for one turn before putting it back?
        prev = None
        while maxHeap:
            # pop from the heap
            entry = heapq.heappop(maxHeap)
            res += entry[1]
            newEntry = (entry[0] + 1, entry[1])
            # add back a prev if its not none
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if newEntry[0] != 0:
                prev = newEntry
        if prev != None or len(s) != len(res):
            return ""
        return res




