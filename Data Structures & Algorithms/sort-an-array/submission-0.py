class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort

        def mergeSort(arr):
            # base case
            if len(arr) == 1:
                return arr # already sorted
            # returns sorted array
            # split the array since itsn ot sorted yet
            mid = len(arr) // 2
            arr1 = mergeSort(arr[0:mid])
            arr2 = mergeSort(arr[mid::])
            return merge(arr1, arr2)


        def merge(arr1, arr2):
            i, j = 0, 0
            res = []
            while len(arr1) > i and len(arr2) > j:
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            
            while len(arr1) > i:
                res.append(arr1[i])
                i += 1

            while len(arr2) > j:
                res.append(arr2[j])
                j += 1
            
            return res
        return mergeSort(nums)
        # divide until sorted (1 element)


        # merging sorted elements together