class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # n tasks labeled from 0 to n - 1
        # each task has enqueueTime and processingTime
        # will be available to process at enqueueTime and takes ProcessingTime to finish

        # simulate enqueuing time
        # we want to grab the least processing time out of all the times that are available to enqueue

        # store the values in a heap by their enquing time, if the curTime >= topOfTheHeapElementEnqueTime pop off and add to a different heap that sorts by processing time.

        # When ur processinng the stuff, simply add the processed index to a result and then jump ur curTimeToTheProcessTime + curTime

        # O(m + nlogn) where m is the max enqueing time and processing time
        enqueueTimeHeap = []
        processingHeap = []

        # store by [enqueueTime, processingTime, index]
        for i,task in enumerate(tasks):
            entry = (task[0],task[1],i)
            # min heap by default
            heapq.heappush(enqueueTimeHeap, entry)
        # print(enqueueTimeHeap)
        # start the curTime at one
        curTime = 1
        res = []
        # continue to do the following while its not empty
        while enqueueTimeHeap or processingHeap:
            
            if processingHeap:
                # stored by [processTime, index]
                entry = heapq.heappop(processingHeap)
                res.append(entry[1])
                # add the processsing time to our current time
                curTime += entry[0]
            if enqueueTimeHeap:
                # if our curTime is not greater than the first element of enqueueTimeHeap
                if not processingHeap and enqueueTimeHeap[0][0] > curTime:
                    print(f'empty process and not high enough time setting to {enqueueTimeHeap[0][0]} {res}')
                    curTime = enqueueTimeHeap[0][0]
                # check for whether we can pop stuff becuase our curTime is >= 0
                while enqueueTimeHeap and enqueueTimeHeap[0][0] <= curTime:
                    entry = heapq.heappop(enqueueTimeHeap)
                    # make a processsHeap element
                    procHeapElement = (entry[1],entry[2])
                    heapq.heappush(processingHeap, procHeapElement)


            
            # check whether processingHeap is empty and enqueueTimeHeap is not empty then we'll have to skip
        return res

            


