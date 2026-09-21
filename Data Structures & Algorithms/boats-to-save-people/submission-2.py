class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        r = len(people) - 1
        l = 0
        res = 0
        while r >= l:
            if people[r] + people[l] > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            res += 1
        return res



