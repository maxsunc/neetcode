class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # number of sub arrrays size k with average >= threshold
        # strict size k

        # fixed sliding window
        # 
        if k > len(arr):
            return 0

        # keep track of the curSum
        curSum = sum(arr[:k])

        left = 0
        res = 0
        #iterate thru the array
        for right in range(k, len(arr)):


        # everytime curSum / k >= threshold add to the result
            if curSum / k >= threshold:
                # print("from " + str(left)  + " to " + str(right))
                res += 1

        # in the sliding window every iteration: subtract from left and add from right
            curSum -= arr[left]
            left += 1
            curSum += arr[right]
        if curSum / k >= threshold:
            # print("from " + str(left)  + " to " + str(right))
            res += 1
        return res