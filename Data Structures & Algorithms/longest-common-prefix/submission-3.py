class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ""
        wordToFollow = strs[0]

        for ind,c in enumerate(wordToFollow):
            for i in range(1,len(strs)):
                s = strs[i]
                if ind >= len(s) or s[ind] != wordToFollow[ind]:
                    return res
            
            res += c
        return res

        
