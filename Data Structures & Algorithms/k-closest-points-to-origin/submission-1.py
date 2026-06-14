class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate the distance and placei nto heap
        heap = []

        for point in points:
            x1,y1 = point[0],point[1]
            dist = (math.sqrt((point[0] )**2 + (point[1])**2))
            # print(f"{dist} for {point}")
            entry = (dist, point)
            heapq.heappush(heap, entry)
        # print(heap)
        res = []
        for i in range(k):
            entry = heapq.heappop(heap)
            res.append(entry[1])
        return res