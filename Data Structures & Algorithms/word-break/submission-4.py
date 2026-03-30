class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # all words in dict are unique
        # we want to see to if all words can be separated into word dict's

        # neetcode
        # ["neet","code"]

        # neetcode
        # ["nee","neet","code"]
        # tcode --> False

        # go backwards, can this string fit?
        # leetcode
        # ["leet","code"]
        wordSet = set(wordDict)
        
        dp = [False for i in range(0, len(s) + 1)]
        dp [len(s)] = True

        for i in range(len(s)-1, -1, -1):
            # check if this substring fits within wordSet if it does
            # check the chunks up
            for j in range(i + 1, len(s) + 1):
                chunk = s[i:j]
                if chunk in wordSet and dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]




