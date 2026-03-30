class Solution:
    def numDecodings(self, s: str) -> int:
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
                return 1
            if s[i] == "0":
                return 0
            if i in saved:
                return saved[i]
            
            val = 0
            if not inBounds(i + 1) or (inBounds(i+1) and s[i+1] != "0"):
                # add one element to curStr
                # print(f"now looking at {s[i+1:]} skip 1")
                val += dfs(i+1)
            
            if inBounds(i+1):
                # build the 2 int
                combined = int(s[i] + s[i+1])
                if 10 <= combined <= 26:
                    # this is also valid !
                    # print(f"now looking at {s[i+2:]}")
                    val += dfs(i+2)
            return val
            
        return dfs(0)
        