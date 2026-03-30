class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. every character of t is within the substring
        # 2. minimium length

        # 3. if the input case isnt valid return "" for now
        # only contains lowercase english letters
        if len(t) > len(s):
            return ""
        # keep track of the t occurance in array of length 26
        # inorder to check whether t is present in the subarray we just check whether the non-zero elements of 
        # tOccurance mach the occurances in the substring

        # O((n) * (n-m)) = O(n^2) assuming m < n 
        # O(1) space though

        # brute force solution
        # fixed sliding windows starting at length t to length s. iterate along until we find a string



        # sacrifice some space for better time complexity
        # dynamic sliding window
        

        # OUZODYXAZVXYZ
        # iterate until the occurances match
        # then reduce from the left until they dont match
        # 
        resLength = len(s) + 1
        res = ""
        # get occurances of s
        tOcc = {}
        for c in t:
            tOcc[c] = tOcc.get(c,0) + 1
        
        sOcc = {}

        # initialize left and right pointers
        left = 0
        for right in range(0, len(s)):
        # iterate through the array
            sOcc[s[right]] = sOcc.get(s[right], 0) + 1
        # add element to occurances


        # keep reducing occurances from the left if the occurances match
            while self.checkOcc(tOcc,sOcc):
            # compare with res the substring
                if right - left + 1 < resLength:
                    resLength = right - left + 1
                    res = s[left:right+1]

            # reduce occurance
                sOcc[s[left]] = sOcc.get(s[left], 0) - 1
                left += 1 
        return res
    def checkOcc(self, tOcc, sOcc):
        # print("Socc")
        # print(sOcc)
        # print("tocc")
        # print(tOcc)
        for key in tOcc:
            # check only the non zwero elements of sOcc if they match
            if tOcc[key] != 0 and sOcc.get(key, 0) < tOcc[key]: # covers case XYZXYZ is a substirng with XYZ
                return False
        return True


