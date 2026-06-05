class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_cnt = {}

        for i in range(len(s)):
            hash_cnt[s[i]] = hash_cnt.get(s[i],  0) + 1
        

        for i in range(len(s)):
            if hash_cnt[s[i]] == 1:
                return i
        
        return -1