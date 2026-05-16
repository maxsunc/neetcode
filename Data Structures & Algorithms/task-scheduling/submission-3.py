class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we have an integer n
        # tasks[i] is an english character from A to Z
        # each cpu cycle only allows completing one task
        # identical tasks must be n cycles apart

        # tasks: array of string
        # n integer

        # return the minimium number of cycles needed to process all of the tasks given the constraint"
        # one task per cycle
        # identical tasks must be separated by at least n cpu cycles

        # process the most frequent task first

        # ["x","x","x","y","y"]
        # x,y,idle,x,y,idle,"x"

        # data structures: track the occurances
        # dictionary: "x" : 2, "y" : 3

        #  tasks = ["A","A","A","B","C"], n = 3

        # O(n * m) where m is the length of tasks
        # ["A" : 3, "B" : 1, "C" : 1]

        # process the most frequent tasks (if not on cooldown)
        # use a heap to find the most frequent tasks
        # once a task is used up: add it to a queue to be added back into the heap at time + n time

        # ["A": 5] ==> m = 5
        # n = 10

        # must return 50
        # we'll just skip forward in time if the heap is over
        # in order ot make this faster we can skip idles
        # if not heap then just grab the leemnt from queue
        
        # 1: count the occurance
        occ = {}
        for task in tasks:
            occ[task] = occ.get(task, 0) + 1
        
        queue = deque() # entry = (occ, val)
        heap = []
        # append of the occurances into heap
        for key in occ:
            entry = (-occ[key],key)
            heapq.heappush(heap, entry) 
        curTime = 0
        # simulate the problem 
        while heap or queue:
            print("running while")
            # check if we can offload from the queue
            while queue and queue[0][1] < curTime:
                # release it since its due
                entry = queue.popleft()
                heapq.heappush(heap, entry[0])
            if heap:
                entry = heapq.heappop(heap)
                print(f"{entry[1]} with {entry[0]}")
                # reduce the time since its spent
                newEntry = (entry[0] + 1, entry[1])
                # add to the queue 
                if -newEntry[0] > 0:
                    queue.append((newEntry, curTime + n))
            elif queue:
                entry = queue.popleft()
                # skip forward in time
                curTime = entry[1]
                heapq.heappush(heap, entry[0])
            curTime += 1



        return curTime

