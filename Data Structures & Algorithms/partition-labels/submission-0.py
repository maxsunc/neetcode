class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # each letter appears at most once in each substring
        # we want the smallest possible substring

        # track the occurance of ech element
        # "xyxxyzbzbbisl"
        # [x:3, y:2,b:3,z:2,i:1,s:1,l:1]

        # [x:3, y:2,]

        # O(n * 26) ==> O(n) time

        # O(26) size ==> O(1) space complexity
        occ = {}
        for c in s:
            occ[c] = occ.get(c,0) + 1
        res = []
        length = 0
        curOcc = {}
        for i in range(0, len(s)):
            c = s[i]
            curOcc[c] = curOcc.get(c,0) + 1
            length += 1

        # 3. check hether curOcc "matches" occ then clear and append to result the length
            matches = True
            for key in curOcc:
                if curOcc[key] != occ[key]:
                    matches = False
                    break
            if matches:
                res.append(length)
                length = 0
                curOcc.clear()
        return res



