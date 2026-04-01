class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # O(n) approach 26 tines faster
        lastIndex = {} # track the last index of each character
        for i,c in enumerate(s):
            lastIndex[c] = i

        # keep updating the end index
        res = []
        length = 0
        end = 0

        for i in range(0, len(s)):
            c = s[i]
            length += 1
            # update the end based on included elements if needed
            end = max(end,lastIndex[c]) # max between prev End and end of the cur char

            # if we're at the end then append
            if i == end:
                res.append(length)
                length = 0
        return res




