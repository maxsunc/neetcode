class Solution:
    def validPalindrome(self, s: str) -> bool:
        # "abbda"
        self.deleted = False



        def is_palin(l, r):
            if l >= r:
                return True
            
            if s[l] != s[r]:
                if self.deleted:
                    return False
                self.deleted = True
                return is_palin(l+1, r) or is_palin(l,r-1)
            else:
                return is_palin(l+1, r-1)

            
        return is_palin(0,len(s)-1)

        # i, j = 0, len(s) - 1

        # while j > i:
        #     print("checking :" + s[i] + " " + s[j])
        #     if s[i] != s[j]:
        #         if deleted:
        #             return False;
        #         deleted = True
        #         if s[i+1] == s[j]:
        #             i += 1
        #         elif s[j-1] == s[i]:
        #             j -= 1
        #         else:
        #             return False

        #     # aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga
        #     j -= 1
        #     i += 1
        # return True
