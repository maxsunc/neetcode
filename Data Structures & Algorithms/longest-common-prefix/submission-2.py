class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find the longest commmon prefix among an array of strings
        if not strs:
            return ""

        # if there is none return ""
        index = 0
        res = ""
        word = strs[0]

        while len(word) > index:
            c = word[index]
            for i in range(0, len(strs)):
                if len(strs[i]) <= index or strs[i][index] != c:
                    return res
            # we made it here
            res += c
            index += 1
        return res