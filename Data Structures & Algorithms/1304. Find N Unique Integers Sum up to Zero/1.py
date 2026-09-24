class Solution:
    def sumZero(self, n: int) -> list[int]:
        # n unique integers that add up to 0

        # n could be even or odd

        # if its odd then one of them must be 0

        # if its even then just count up starting from both sides til they cross

        res = [0 for i in range(0,n)]

        r,l = len(res) - 1, 0
        counter = 1

        while r >= l:
            if r == l:
                # make this 0
                res[r] = 0
            else:
                # make both inverses of each other
                res[r] = counter
                res[l] = -counter

            counter += 1
            r -= 1
            l += 1
        return res