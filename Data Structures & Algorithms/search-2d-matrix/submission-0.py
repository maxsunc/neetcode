class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on row

        # binary search on columns
        l, r = 0, len(matrix)-1

        while(r >= l):
            
            mid = int(l + (r-l)/2)
            value = matrix[mid][0]
            print(f'searching {value}')
            if matrix[mid][0] == target:
                return True
            if value > target:
                r = mid - 1
            else:
                l = mid + 1

        # now l and r should be the same, do binary search on that row
        row = l - 1
        l = 0
        r = len(matrix[0]) - 1
        while (r >= l):

            mid = int(l + (r-l)/2)
            value = matrix[row][mid]
            print(f'searching 2 {value}')

            if value == target:
                return True
            if value > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

