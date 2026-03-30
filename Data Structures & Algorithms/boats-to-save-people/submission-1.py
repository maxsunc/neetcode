class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people [i]
        # boats can only carry 2 people

        # limit = weight limit of boat
        # find minimum number of boats it takes to carry each person

        # [5,1,4,2]
        # limit 6: [5,1], [4,2]


        # brute force: look for max value then find fitting person. O(n^2)

        # sort the array O(nlogn)
        # better solution: sort this arraynow we have access to heaviest person and lightest person
        # have two pointers (one at front and one at back)
        
        # each time aboat is sent advance both pointers

        # [1,2,4,5]

        # [1,2,2,3,3]

        # case 1: heavy person takes up all space (only advance left most)
        # case 2: heavy person and light person fit, (advance both pointers)
        
        # repeat this until pointers cross

        people.sort()
        r = len(people) - 1
        l = 0
        res = 0
        while r >= l:
            if people[r] + people[l] > limit:
                print(f"{people[r]}")
                # only advance right pointer
                r -= 1
            else:
                print(f"{people[l]} + {people[r]}")
                # both people fit
                r -= 1
                l += 1
            res += 1
        return res



