class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1,0,2,3,6,8] target = 4 
        if nums[0] == target:
            return 0
        
        l,r = 0, len(nums)-1

        if nums[r] == target:
            return r

        mid = int((r-l)/2)
        while(True):
            if mid == l or mid == r:
                break
            value = nums[mid]
            if value == target:
                return mid

            if value > target:
                r = mid
                print("hello2")
            else:
                l = mid
                print("hello")
            
            mid = int((r-l)/2) + l

        return -1



        