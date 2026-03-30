class TimeMap:


# store key value pairs at time stamps
# each time stamp can only support one unique key value pair
# t = 2: "alice", "happy", "jerry", "sad"
    def __init__(self):
        # store a hashmap with key and the value as an array of tuples (timestamp, value)
        self.myMap = defaultdict(list) # default each value to a list

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add a key 
        # strictly increasing means each set means new timestamp
        
        self.myMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        # we know where to look, at key
        # inside of key's values it is sorted (guarunteed) perform binary search on those values
        search = self.myMap[key]
        print('called get on ' + str(search) + " with searching for " + key + " at " + str(timestamp))

        l, r = 0, (len(search) - 1)
        recentValue = ""
        # search for timestamp
        while r >= l:
            mid = (r+l) // 2
            # ("green", 1), ("red", 3), ("purple", 4)
            if search[mid][0] == timestamp:
                return search[mid][1]
            elif search[mid][0] > timestamp:
                r = mid - 1
            else:
                # search[mid][0] < timestamp
                l = mid + 1
                recentValue = search[mid][1]
        
        return recentValue


                




