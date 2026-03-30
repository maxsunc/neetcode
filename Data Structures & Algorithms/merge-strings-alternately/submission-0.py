class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        reze = ""

        i = 0

        while i < min(len(word1), len(word2)):
            reze += word1[i] + word2[i]
            i += 1
        
        while i < len(word1):
            reze += word1[i]
            i += 1

        while i < len(word2):
            reze += word2[i]
            i += 1
        return reze