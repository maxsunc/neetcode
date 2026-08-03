class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # can do this in nlogn time
        # sort it
        # iterate k times and retunr that vlaue
        # this is the brute force

        for i in range(len(nums)):
            nums[i] *= -1
        # O(klogn)
        heapq.heapify(nums)

        for i in range(0, k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
