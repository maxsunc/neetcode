class TimeMap:


# store key value pairs at time stamps
# each time stamp can only support one unique key value pair
# t = 2: "alice", "happy", "jerry", "sad"
    def __init__(self):
        # are the timestamps stritly increasing?
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp)) # assume timestamp is always increasing so no need to reorder

    def get(self, key: str, timestamp: int) -> str:
        # log(n) algorithm used to get the vlaue at the timestamp or the below one
        # rememebr r and l will be crossed, r is below l

        # get tehe array we want to search
        arr = self.map[key]

        l, r = 0, len(arr) - 1

        while r >= l:
            # mid point calc
            m = (l + r) // 2
            entry = arr[m]

            # check if the timestamp matches
            if entry[1] == timestamp:
                return entry[0]
            elif entry[1] > timestamp:
                r = m - 1
            else:
                l = m + 1
        return arr[r][0] if r >= 0 else ""
        
        # [("alice",1), ("bob",3), ("kevin",6)]
            



                




