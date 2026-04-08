class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # s3 is interleaving s1 and s2

        # divide s1 and s2 into substring that go well into s3


        # aabbbbaa

        # aaaa
        # bbbb
        if len(s1) + len(s2) != len(s3):
            return False

        # two pointers on each of the strings
        # if only one string matches then advance that pointer and main pointer
        # if both work then check both cases if it works recursive
        memo = {}
        def dfs(i, l, r):
            if i == len(s3):
                return True
            verdict = False
            if (l,r) in memo:
                return memo[(l,r)]
            # if both of them match explore both cases
            if (l < len(s2) and r < len(s1)) and s1[r] == s3[i] and s2[l] == s3[i]:
                # choose either to advance
                verdict = dfs(i+1, l + 1, r) or dfs(i + 1, l, r + 1)
                return verdict
            # only one of them is available
            elif l < len(s2) and s2[l] == s3[i]:
                verdict = dfs(i+1, l + 1, r)
            elif r < len(s1) and s1[r] == s3[i]:
                verdict = dfs(i+1, l, r + 1)

            memo[(l,r)] = verdict
            return verdict

        return dfs(0,0,0)



                
