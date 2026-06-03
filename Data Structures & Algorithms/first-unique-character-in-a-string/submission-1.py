class Solution:
    def firstUniqChar(self, s: str) -> int:

        hash_store = {}


        for n in s:
            hash_store[n] = hash_store.get(n, 0) + 1
        

        for i in range(len(s)):
            if hash_store[s[i]] == 1:
                return i
        
        return -1
        