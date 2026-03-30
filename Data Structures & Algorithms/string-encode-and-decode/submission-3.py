class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode using length of thing + # 
        # we say : yes ==> 2#we3#say1#:3#yes
        # 
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += f"{length}#{s}" 

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        print(f"decoding {s}")
        i = 0
        while i < len(s):
            # 2#we3#say1#:3#yes
            # unpack into a list
            # read as a number
            lengthAsStr = ""
            while s[i] != "#":
                print(f"adding {s[i]}")
                lengthAsStr += s[i]
                i += 1
            print(lengthAsStr)
            if lengthAsStr == "":
                print("breaking at " + lengthAsStr)
                break
            # c = #
            if i < len(s):
                i += 1
            length = int(lengthAsStr)
            # c = some letter
            # loop lengthAs
            strToAdd = s[i:length+i]
            i += length
            
            result.append(strToAdd)

        return result


