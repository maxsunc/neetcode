class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        # find the distance from origin to each of hte points
        heap = []
        for point in points:
            # everytime we are full remove that element from the heap and add it to our result
            distance = point[0] * point[0] + point[1] * point[1]
            entry = [-distance, point[0], point[1]]
            heapq.heappush(heap, entry)

            if len(heap) > k:
                
                # remove the element and add the point to res
                heapq.heappop(heap)
        
        # n + klogn 
        # now we have the k elements
        while heap:
            d,x,y = heapq.heappop(heap)
            res.append([x,y])
        # reorganize in a heap format
        return res

        # grab first k elements

        # remove points when size exceeds k
