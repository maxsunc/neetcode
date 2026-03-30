class Solution:
    def mySqrt(self, x: int) -> int:
        # linearly check from 1 - 9 if
        # i * i >= 9 then return

        # alternatively, instead of linear we can transform this into a binary search 
        # since 1-9 is sorted
        # 5 --> 2(.5) --> 3(.5)
        l, r = 1, x
        res = 0

        while r >= l:
            m = (r + l) // 2
            squared = m * m
            if squared == x:
                return m
            elif squared > x:
                r = m - 1
            else:
                l = m + 1
                res = m
        # 1,13 --> 1,6 --> 4,6 --> 4,4 --> 4,3
        # 1,2, 2,2, 2,1
        return res