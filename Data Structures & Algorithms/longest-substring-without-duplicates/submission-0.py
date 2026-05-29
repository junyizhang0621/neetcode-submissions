class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        i, j = 0, 1
        res = s[i:j]
        max_result = 0

        while j < len(s):
            lc = s[i]
            rc = s[j]

            if rc not in res:
                res =s[i:j+1]
                j += 1
                max_result = max(max_result, len(res))
            else:
                i += 1
                if i == j:
                    j+=1
                res = s[i:j]
        max_result = max(max_result, len(res))
        
        return max_result

        