class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # sort the array
        piles.sort()

        # start with k = max(piles)
        k = piles[len(piles) - 1]

        # perform binary search for a new k value, do it until binary search is done
        l, r = 0, k
        def verifyIsGood(kVal):
            if kVal == 0:
                return False
            counter = 0
            for i in piles:
                counter = counter + math.ceil(i/kVal)
            if counter <= h:
                return True
            return False



        while(r >= l):
            # maxVal = 11
            # 11/2 = 5
            # 5/2 = 2
            # 7/2 = 3
            # 8/2 = 4
            m = int(l + (r-l) / 2)

            verdict = verifyIsGood(m)

            if verdict:
                r = m - 1
                k = m
            else:
                l = 1 + m

        return k

