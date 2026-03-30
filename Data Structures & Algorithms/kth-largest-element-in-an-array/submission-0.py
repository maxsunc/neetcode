class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # turn into a max heap
        for i in range(0,len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        # heap pop 
        for i in range(1,k):
            print(len(nums))
            heapq.heappop(nums)

        return nums[0] * -1