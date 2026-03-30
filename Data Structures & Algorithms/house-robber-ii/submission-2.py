class Solution:
    def rob(self, nums: List[int]) -> int:
        # take 

        # previously:
        

        # flag whether the took the first value or not
        # in the bottom up approach use a tuple
        
        # in the recursive use a flag parameter
        saved = {}
        def dfs(i, tookFirst):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                if not tookFirst:
                    return nums[i]
                else:
                    return 0
            
            # recurrsive case
            if (i,tookFirst) in saved:
                return saved[(i,tookFirst)]
            val = 0
            val = max(dfs(i + 2, tookFirst) + nums[i], dfs(i+1, tookFirst))
            print(f"val is {val} for {nums[i:]} {tookFirst}")
            saved[(i,tookFirst)] = val
            return val
        return max(dfs( 2, True) + nums[0], dfs(1, False))