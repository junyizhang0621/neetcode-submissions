class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        char_count = {}
        res = 0

        l, r = 0,0

        while r < len(s):
            if s[r] not in char_count or char_count[s[r]] == 0:
                char_count[s[r]] = 1
            else:
                char_count[s[r]] += 1
            
            while (r - l + 1) - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r+= 1
        return res

                
        