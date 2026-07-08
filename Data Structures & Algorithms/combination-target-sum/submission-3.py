class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # may be chosen an unlimited number of times
        # take this value of continue to next: two decision

        #base case is if the value == the target: return 1, since we found one way
        # if the value > target: return 0: (this is invalid)
        # also if the 
        nums.sort()
        

        # either take or no take

        # backtracking:

        # 2^ (n * m/l))
        
        # memoize the result by checking the current sum
        res = []
        def dp(curSum, i, curComb):
            nonlocal res
            if curSum == target:
                print(f"found one at {curComb}")
                res.append(curComb.copy())
                return
            elif curSum > target or i == len(nums):
                return
            
            # two cases: stay here and add one or advance
            curComb.append(nums[i])
            dp(curSum + nums[i],i, curComb)
            curComb.pop()
            dp(curSum, i + 1, curComb)
        
        dp(0,0,[])
        return res