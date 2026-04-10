class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1 and word2
        
        # find the minimium number of operations

        # monkeys
        # money


        # insert
        # delete
        # replace 

        # three cases:

        # 1st case len(word1) == len(word2): 
        # need replacements at different places only 

        # when word matches proceed thats free

        # when word doesnt match either remove or replace iwth the right word
        # two pointers 
        # 
        # replacement: advance both pointers
        # deletion means advance only first pointer 
        # amoney
        # mmoney
        # money 

        # use insertion when exhausted all of word1: i == len(word1)
        # AND j != len(word2) (still have to create word2):
        # len(word2) - j insertions needed 

        # memoization of i,j
        memo = {}
        def dfs(i,j):
            # base cases:
            if j == len(word2):
                if  i == len(word1):
                    return 0
                else:
                    return len(word1) - i
            if i == len(word1):
                # need insertions to get to the end
                return len(word2) - j
            if (i,j) in memo:
                return memo[(i,j)]
            val = 0
            # recursive cases
            # 1: Both equalling eachother proceed with no cost
            if word1[i] == word2[j]:
                val =  dfs(i + 1, j + 1)
            else:
                # they're not equal to eachother 
                # either replace ( advance both) or delete (advance first pointer)
                val = min(1 + dfs(i + 1, j), 1 + dfs(i + 1, j + 1), 1 + dfs(i, j + 1))
            memo[(i,j)] = val
            return val
        return dfs(0,0)
        # money



