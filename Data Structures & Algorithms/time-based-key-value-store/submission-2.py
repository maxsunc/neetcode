class TimeMap:

    def __init__(self):
        # storing multiple values for the samek ey at specifiewd time stamps

        # retrieving the key's value at specified time stamps
        # key : [(Timestamp, value),]
        self.entries = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        # stores key with value value at given timestamp
        # strictly increasing order --> NO editting
        entry = (timestamp,value)
        self.entries[key].append(entry)



    def get(self, key: str, timestamp: int) -> str:
        # returns the omst recent value from key from the most recent timestamp
        # prevTimestamp <= timestamp (largestest prevTimestamp)

        # if there isnt one then return ""
        arr = self.entries.get(key, [])
        if len(arr) == 0 or arr[0][0] > timestamp:
            return ""

        # we know there is a valid answer
        # perform binary search
        l,r = 0, len(arr) - 1
        index = 0
        # 4
        # [1,"dog"],[3:"tarp"],[7,"car"]
        while r >= l:
            mid = l + (r-l) // 2
            if arr[mid][0] <= timestamp:
                index = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return arr[index][1]



        
