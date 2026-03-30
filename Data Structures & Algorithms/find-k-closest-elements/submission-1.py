class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # closer condition:1: |a - x| < |b - x|, or
        #2: |a - x| == |b - x| and a < b
        # prefers lower values if distance is same
        # 1 < 2 ==> 5 dominates 8
        # 2 == 2
        # 4 < 8 ==> 4 dominates
        res = []
        
        placeToInsertBefore = -1
        # find the two pointers
        for i in range(0,len(arr)):
            if arr[i] >= x:
                placeToInsertBefore = i
                break

        if placeToInsertBefore == -1:
            # insert at the end
            placeToInsertBefore = len(arr) 
        
        right = placeToInsertBefore
        left = placeToInsertBefore-1
        # iterate k times to get k closest elemnts
        for i in range(0, k):
            closestElement = 0
            if right >= len(arr):
                closestElement = arr[left]
                left -= 1
            elif left < 0:
                closestElement = arr[right]
                right += 1
            else:
                print("comparing " + str(arr[left]) + " and " + str(arr[right]))
                # calculate it, both left and rigth are available
                if abs(arr[left] - x) < abs(arr[right] - x):
                    # left is the one
                    closestElement = arr[left]
                    left -= 1
                else:
                    # check equality, otherwise right is the one
                    if abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right]:
                        closestElement = arr[left]
                        left -= 1
                    else:
                        closestElement = arr[right]
                        right += 1
            res.append(closestElement)
        res.sort()
        return res




