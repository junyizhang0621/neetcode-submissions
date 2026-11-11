class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check_hash = {}
        for i in t:
            check_hash[i] = check_hash.get(i, 0) + 1
        
        find_hash = {}

        find, target = 0, len(check_hash)

        l, r = 0, 0
        res = ""

        min_length = float('inf')
        while r < len(s):
            find_hash[s[r]] = find_hash.get(s[r], 0) + 1
            if find_hash[s[r]] == check_hash.get(s[r], 0):
                find += 1
            while find == target:
                if (r - l + 1) <= min_length:
                    min_length = (r - l + 1)
                    res = s[l:r + 1]
                find_hash[s[l]] -= 1
                if find_hash[s[l]] < check_hash.get(s[l], 0):
                    find -= 1
                l += 1
            
            r += 1
        return res

