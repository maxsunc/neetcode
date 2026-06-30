class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, len(arr) - 1

        while r - l + 1 > k: # window size is greater than k
            # check the right vs the left
            # print(r)
            if abs(arr[r] - x) >= abs(arr[l] - x):
                r -= 1
            else:
                l += 1
        return arr[l : r + 1]


        # l,r = 0, len(arr) - 1
        # while r >= l:
        #     mid = l + (r - l) // 2
        #     if arr[mid] > x:
        #         r = mid - 1
        #     else:
        #         l = mid + 1

        # # l is always across the r
        # l,r = l,l

        # while (r - l + 1) < k:
        #     # increase the window size based on the values
        #     if r + 1 < len(arr) and l - 1 >= 0:
        #         val1,val2 = arr[r+1],arr[l-1]
        #         dist1,dist2 = abs(val1 - x), abs(val2 - x)
        #         if dist1 >= dist2:
        #             # take val2
        #             l -= 1
        #         else:
        #             r += 1
        #     elif r + 1 < len(arr):
        #         # advance r
        #         r += 1
        #     else:
        #         l -= 1
        # return arr[l : r + 1]