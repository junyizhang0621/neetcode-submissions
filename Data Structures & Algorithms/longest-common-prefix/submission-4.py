class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""

        longest = len(strs[0])

        for i in range(longest):
            cur_s = strs[0][i]
            for s in strs:
                if i >= len(s):
                    return res
                if s[i] != cur_s:
                    return res

            res += cur_s 
        return res