class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # neet
        # teen
        # teen
        # fives
        # sivef
        # sevif

        i = 0
        j = len(s)-1

        while j > i:
            # swap values in place
            tmp = s[i]
            s[i ] = s[j]
            s[j] = tmp


            i += 1
            j -= 1