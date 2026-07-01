class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # min operations to make the array empty
        # immediantly return -1 if any occurance is <= 1
        # count the occurances: 
        # for each occurance we see we want to reduce it minimally
        def evaluateMinOps(val):
            if val % 3 == 0:
                return val // 3
            else:
                # # val % 3 == 1:
                # value = evaluateMinOps(val - 3)
                # print(value)
                # return value + 1
                return (val // 3) + 1
            

        occ = {}
        for num in nums:
            occ[num] = occ.get(num,0) + 1
        res = 0
        for key,val in occ.items():
            if val <= 1:
                return -1
            # return 0
            
            # break it down into 2s and 3s
            # 
            # if (val % 3) % 2 != 0 and val % 2 != 0:
            #     print(f"failed for {val}")
            #     return -1
            # now we know it can be made up of 3s and two 
            # count 3s
            valToAdd = evaluateMinOps(val)
            print(f"min ops for {val} is {valToAdd}")
            res += valToAdd
        return res
            