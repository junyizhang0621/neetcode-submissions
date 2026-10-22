class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i)) + "#"
            res += i
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        index = 0

        while index <len(s):
            
            j = index

            while s[j]!= "#":
                j += 1 
            char_count = int(s[index:j])
            index = j + 1
            res.append(s[index: index + char_count])
            index += char_count
        
        return res