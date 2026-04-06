class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # length of the longest common subsequence betweeen 2 strings
        # dp solution bottom up approach

        # if they match that is basically "free" we should always take it since they match: 
        dp = [[0 for i in range(0,len(text2))] for j in range(0, len(text1))]

        # iterating thru the dp table 
        for i in range(0,len(dp)):
            for j in range(0,len(dp[0])):
                if text1[i] == text2[j]:
                    dp[i][j] = 1
                    if i != 0 and j != 0:
                        dp[i][j] += dp[i-1][j-1]
                else:
                    # get the max of both up and down
                    if i != 0:
                        dp[i][j] = dp[i-1][j]
                    if j != 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])
        
        return dp[len(text1)-1][len(text2)-1]