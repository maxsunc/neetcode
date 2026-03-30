class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the target and return the index other wise return -1 if it doesn't exist

        # follow-up what if we wanted the closest index down?
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        while r >= l:
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m -1
            else:
                l = m + 1
            m = (l + r) // 2
        return -1