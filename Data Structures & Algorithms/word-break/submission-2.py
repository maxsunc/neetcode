class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # all words in dict are unique
        # we want to see to if all words can be separated into word dict's

        # neetcode
        # ["neet","code"]

        # neetcode
        # ["nee","neet","code"]
        # tcode --> False
        wordSet = set(wordDict)


        # backtracking solution to try every single substring but this is too slow 

        # convert wordDict into an  for O(1) access time
        reze = False
        memo = set()
        # nee
        def dfs(i, curStr):
            nonlocal reze
            # if we're at the end and our curStr isn't empty then return False (not possible)
            # if we're at the end and curtr is empty then Return True
            if i == len(s):
                if len(curStr) == 0:
                    reze = True
                return
            curStr += s[i]
            if (i,curStr) in memo:
                return
            memo.add((i,curStr)) # already saw this path dont need to look thru it again
            # print('hi')
            # recurrsive case take or not take when a word is aailalbe
            if curStr in wordSet:
                # we have two options: 
                # 1. Reset curStr
                # 2. Don't reset curStr
                # print(f"took {curStr}")
                dfs(i+1, "")
            dfs(i+1, curStr) # don't reset
        dfs(0, "")
        return reze
        


