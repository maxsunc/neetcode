import sys
sys.setrecursionlimit(10000)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # find the number of distinct subsequences of s equal to t
        # 

        # caaat

        # cat

        # if it works we have two options:
        # take or skip

        # if the words dont match then skip
        memo = {}
        
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s): # we're at the end of s but not at end of t
                return 0 # no way of building t

            if (i,j) in memo:
                return memo[(i,j)]


            distinct = 0
            if s[i] == t[j]:
                distinct += dfs(i + 1, j + 1)
            distinct += dfs(i + 1, j)
            memo[(i,j)] = distinct
            return distinct 


        return dfs(0,0)
            