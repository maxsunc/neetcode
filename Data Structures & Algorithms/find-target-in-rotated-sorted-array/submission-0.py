class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Phase 1: find the point it was rotated at  using binary search
        def findNumRotates():
            l, r = 0, len(nums) - 1
            minVal = nums[0]
            index = 0
            # [3,4,5,6,1,2]
            while r >= l:
                m = (l + r) // 2
                if nums[m] <= nums[r]:
                    # new min
                    if nums[m] < minVal:
                        minVal = nums[m]
                        index = m
                    r = r - 1
                else:
                    l = l + 1
            
            return index
                
        offset = findNumRotates()
        print(offset)
        # Phase 2: Perform binary search with an offset
        l, r = 0, len(nums) - 1
        # normal binary search but with an offset
        m = 0
        while r >= l:
            m = (l + r) // 2
            mOff = (m + offset) % len(nums)
            rOff = (r+offset) % len(nums)
            val = nums[mOff]
            print(f"checking {val} at {m}")
            if val == target:
                return mOff
            elif val > target:
                r = m - 1
            else:
                l = m + 1
            print((l,r))
            # [1,2,3,4,5,6]
            # [3,4,5,6,1,2]

        
        return -1


        # results in a O(2logn) solution which simplifies to logn

