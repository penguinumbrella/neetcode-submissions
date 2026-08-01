class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        #print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            # get the len of the string
            while s[j] != "#":
                j += 1
            #print(i, j)
            length = int(s[i:j])

            string = s[j + 1 : j + length + 1]
            #print(string)
            result.append(string)
            #print(result)
            i = j + length + 1
        return result
