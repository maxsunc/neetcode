class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        i, j = 0, 0

        while m > i and n > j:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
        
        while m > i:
            tmp.append(nums1[i])
            i += 1
        
        while n > j:
            tmp.append(nums2[j])
            j += 1
        

        for i in range(0, len(nums1)):
            nums1[i] = tmp[i]