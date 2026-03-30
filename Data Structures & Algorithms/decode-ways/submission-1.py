class Solution:
    def numDecodings(self, s: str) -> int:
        print(s)
        saved = {}
        # print('hi')
        # 123
        def inBounds(i):
            return 0 <= i < len(s)
        # [1]
        res = 0
        def dfs(i):
            # print("called ???")
            nonlocal res
            if i >= len(s):
                res += 1
                return
            if s[i] == "0":
                print("found a 0 fudge")
                return
            
            val = 0
            if not inBounds(i + 1) or (inBounds(i+1) and s[i+1] != "0"):
                # add one element to curStr
                # print(f"now looking at {s[i+1:]} skip 1")
                dfs(i+1)
            
            if inBounds(i+1):
                # build the 2 int
                combined = int(s[i] + s[i+1])
                if combined <= 26:
                    # this is also valid !
                    # print(f"now looking at {s[i+2:]}")
                    dfs(i+2)
        dfs(0)
        return res

            

        