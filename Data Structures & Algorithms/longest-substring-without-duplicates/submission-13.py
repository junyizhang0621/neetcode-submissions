class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        res = 0
        l, r = 0, 0
        check_hash = {}

        while r < len(s):
            if s[r] not in check_hash or check_hash[s[r]] == 0:
                res = max(res, r - l+1)
                check_hash[s[r]] = check_hash.get(s[r], 0) + 1
                r += 1
            else:
                check_hash[s[l]] -= 1
                l+= 1
        
        return res



