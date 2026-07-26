class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # merges two sorted arrays
        def merge(left, mid, right):
            # sorted arrays are from left to mid and mid + 1 to right
            temp1, temp2 = [],[]

            # add the stuff to temp1 temp2
            for i in range(left, mid + 1):
                temp1.append(nums[i])
            for i in range(mid + 1, right + 1):
                temp2.append(nums[i])
            
            # go from left to right inclusive: while iterating thru temp1 temp2 adding the min element
            i,j = 0,0
            index = left
            while len(temp1) > i and len(temp2) > j:
                if temp1[i] > temp2[j]:
                    nums[index] = temp2[j]
                    j += 1
                else:
                    nums[index] = temp1[i]
                    i += 1
                index += 1
            
            while len(temp1) > i:
                nums[index] = temp1[i]
                i += 1
                index += 1
            while len(temp2) > j:
                nums[index] = temp2[j]
                j += 1
                index += 1
            


        def mergeSort(left, right):
            # divide the array in 2 and call merge sort of both halves then merge them
            if right > left:
                mid = (right + left) // 2
                mergeSort(left, mid)
                mergeSort(mid + 1, right)
                merge(left, mid, right)
        mergeSort(0,len(nums)- 1)
        return nums