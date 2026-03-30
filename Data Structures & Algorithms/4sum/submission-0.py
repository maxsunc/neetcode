class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort for free
        # O (n^3)
        # for each target value call 3sum on it
        # four digits add up to a target
        # return ALL UNIQUE quadruplets
        # 
        # strictly looking at the values that can be added
        # nums :int array
        # every single unique quadruplet (4 digits) that add up to target
        # (the values ditinguish sets (NOT THE INDEXES))
        nums.sort()
        # space or time
        seenQuad = set()
        res = []
        # sort O(nlogn)
        # [-3,0,1,2,3,3]
        # iterate through the array O(n) (i)
        for i in range(0, len(nums)):
            newTarget = target - nums[i]
            subNums = nums[i+1:len(nums)]
            print(subNums)
            triplets = self.threeSum(subNums, newTarget)
            if len(triplets) != 0:
                for t in triplets:
                    quad = list(t)
                    quad.append(nums[i])
                    # print("adding "+ str(quad))
                    tup = tuple(quad)
                    if tup not in seenQuad:
                        seenQuad.add(tup)
                        res.append(quad)
        return res
                    

        # call threesum on smaller subarray with target as -nums[i] (returns a list of lists)
        # how to check valid quadruplet?""
    
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 0,1,2,3,3
        res = set()
        # seenTriplets = set() # set of tuplets
        # iterate thru the array (i) O(n)
        for i in range(0, len(nums)):
            newTarget = target - nums[i]
            l,r = i + 1, len(nums) - 1
            # two pointer to find pairs for the triplet
            while r > l:
                pairSum = nums[l] + nums[r]
                triple = (nums[i],nums[l],nums[r])
                if newTarget == pairSum:
                    # print(f"{nums[l]} + {nums[r]} is {newTarget}")
                    triplet = (nums[i], nums[l], nums[r])
                    res.add(triplet)
                    # seenTriplets.add(triple)
                    l += 1
                    r -= 1
                elif pairSum > newTarget:
                    r -= 1
                else:
                    l += 1
        return list(res)
            

                    
        # foreach value in the array find 2 indexes that add up to the target - nums[i] O(N)

        # O(n^2)
        
