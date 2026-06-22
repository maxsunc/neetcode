class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # [2,7,15] => [1 day, 7 day, 30 day]

        # backtrcking

        # test all situations dp:

        # keep track: lastDay we're covered, currentIndex
        # curCost
        # on now add memo
        memo = {}
        def backtrack(lastDay, i):
            if i == len(days):
                return 0 # we're done
            if (lastDay, i) in memo:
                return memo[(lastDay,i)]
            
            # recursive case: Try all
            # case 1: our lastDay is bigger than or equal to our day[i]
            # print(f"{lastDay}")


            if lastDay >= days[i]:
                val = backtrack(lastDay, i + 1)
                memo[(lastDay,i)] = val
                return val
            else:
                # print("END")
                # case 2: where we need to buy a pass
                # try all options of buying passes
                minVal = min(
                    backtrack(days[i], i + 1) + costs[0],
                    backtrack(days[i] + 6, i + 1, ) + costs[1],
                    backtrack(days[i] + 29, i + 1 ) + costs[2]
                )
                memo[(lastDay,i)] = minVal
                return minVal

        return backtrack(0,0)