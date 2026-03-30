class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''

        for i in range(0, len(strs[0])):
            currentLookingChar = strs[0][i]
            exit = False
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or currentLookingChar != strs[j][i]:
                    exit = True
                    break
            if exit:
                break
            else:
                result += currentLookingChar

        return result