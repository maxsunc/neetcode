class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2+ zero => 0000
        # 1 zero => everything else is 0
        # 0 zeros => everything has a value > 0 

        # dont need to care about division since no dividing 0 is happening
        prefixProd = [1] * (len(nums))
        suffixProd = [1] * (len(nums))
        

        # build the suffix and prefix arrays

        # build the prefix, product of everything behind that index
        for i in range(1,len(nums)):
            prefixProd[i] = prefixProd[i-1] * nums[i-1]
            # [1,2,4,6]
            # [  1,2,8]
        
        #build the suffix arrays
        for i in range(len(nums)-2, -1, -1):
            suffixProd[i] = suffixProd[i+1] * nums[i+1]
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = prefixProd[i] * suffixProd[i]
        return result


        
            




