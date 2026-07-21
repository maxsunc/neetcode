class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # dp problem: Try all scenerios
        
        # n jobs where each job is from startTime to endTime with profit[i]
        # its not duration, it is a interval

        # find the maximum profit we can take such that no two jobs are overlapping

        # create an intervals array where each element is [startTime, endTime, profit]
        # sort by startTime 
        # we have a decision to either take or dont take at each interval.
        # after we take it, we need to increment until the startTime is >= the endTime of the taken interval

        # dp comes in by finding the maxProfit AT an interval (i think this is the way we can memoize this?)
        entries = []
        

        # guarunteed the array startTime, endTime and profit are the same length
        for i in range(0, len(startTime)):
            entry = (startTime[i],endTime[i],profit[i])
            entries.append(entry)
        # sort it O(nlogn)
        entries = sorted(entries, key=lambda x: x[0])
        # print(entries)
        # this approach right now is 2^n since each guy has two decisions, in the worst case where none are overlapping
        # make this memoized
        memo = {}
        n = len(entries)



        def backtrack(i):
            # get to the end, return 0
            if i >= n:
                # print('bru')
                return 0
            if i in memo:
                return memo[i]
            
            # take or don't take
            dontTake = backtrack(i + 1) 
            start,end,profit = entries[i]
            take = profit
            
            # instead of doing this, search with binary search to see 
            # move to the i that has start >= end
            # search for the element index of the entry with max start >= end
            l, r = i + 1, len(entries) - 1
            minIndex = r + 1
            while r >= l:
                mid = l + (r-l) // 2
                if entries[mid][0] >= end:
                    minIndex = mid
                    r = mid - 1
                else:
                    l = mid + 1
            if minIndex <= n - 1:
                take += backtrack(minIndex)
            # print(f"comparing {take} vs {dontTake}")
            res = max(take, dontTake)
            memo[i] = res
            return res
        return backtrack(0)
            

