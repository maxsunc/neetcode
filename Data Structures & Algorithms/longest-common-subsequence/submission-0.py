class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # length of the longest common subsequence betweeen 2 strings

        # "cat" and "crabt"
        # ==> cat is the answer

        # either delete and element or dont delete the element

        # take or no take

        # []

        # if the character at current index both match then proceed with both cuz thats just free

        # else: proceed on either index
        memo = [[-1 for j in range(0,len(text2))] for i in range(0,len(text1))]
        def dfs(i,j):
            # base case
            if i == len(text1) or j == len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            val = 0
            if text1[i] == text2[j]:
                # proceed this is free
                val = 1 + dfs(i+1,j + 1)
            else:
                val = max(dfs(i+1,j), dfs(i,j+1))
            memo[i][j] = val
            return val
        # print(memo)
        return dfs(0,0)