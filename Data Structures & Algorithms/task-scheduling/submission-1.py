class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # n cycle cooldown
        if not tasks:
            return 0
        # 1. keep track of each letter's occurances store it in a hashmap
        occurances = {}

        for task in tasks:
            occurances[task] = occurances.get(task,0) + 1




        maxHeap = []

        for val in occurances.values():
            maxHeap.append(-val)

        heapq.heapify(maxHeap)


        queue = deque()
        curTimestamp = 0

        # create a maxHeap (negative min heap) 
        while maxHeap or queue:
            curTimestamp += 1
            if queue and queue[0][0] <= curTimestamp:
                entry = queue.popleft()
                heapq.heappush(maxHeap,entry[1])
        # heap should be by frequency only (one value)
        # everytime we take off from the top
        # send it to the queue with (time it comes off, frequenecy)
            if maxHeap:
                # pop from the queue
                freq = heapq.heappop(maxHeap)
                print(freq)
                freq += 1 # cuz negative
                if freq != 0:
                    entry = (curTimestamp + n + 1, freq)
                    queue.append(entry)
            else:
                print("empty")
        # loop until maxHeap and q is empty

        # in the loop:

        # increment currentTimestamp
        # check if we can add top of the q value to heap(heappush)
        return curTimestamp
        # take off the top value from the heap



        # maxKey = ""
        # maxValue = -1
        # for task in occurances:
        #     if occurances[task] > maxValue:
        #         maxKey = task
        #         maxValue = occurances[task]

        # # 2. create a heap based on next available timestamp (all -1 right now)
        # minHeap = []
        # # start at the max value (of occurances)
        # entry = (-1, maxKey)
        # minHeap.append(entry)
        # # append all the other value in occurances
        # for task in occurances:
        #     if task == maxKey:
        #         continue
        #     minHeap.append((-1,task))


        # # 3. keep a current timestamp at 0
        # curTimestamp = 0

        # while minHeap:
        #     curTimestamp += 1
        #     # check if we can take off the top value of the heap
        #     if minHeap[0][0] < curTimestamp:
        #         print(minHeap[0][1])
        #         key = minHeap[0][1]
        #         # decrement it
        #         occurances[key] -= 1
        #         entry = heapq.heappop(minHeap)

        #         # case where we need to add it back
        #         if occurances[key] > 0:
        #             # recalculate the valiue at the top and heapify it again
        #             # pop and add back
        #             newEntry = (curTimestamp + n, entry[1])
        #             # heap command here
        #             heapq.heappush(minHeap, newEntry)
        #     else:
        #         print("empty")
        #     # A, A, A

        # # 4. increment one for each decrement we call onto a value in heap
        # # everytime a value is decremented in leastInterval (check if value == 0 then pop)
        # # each decremeent of a value causes the next available timestamp to increase to currentTimestamp + n

        # # repeat until the heap is empty
        # return curTimestamp


        # return currentTimestamp
        

        