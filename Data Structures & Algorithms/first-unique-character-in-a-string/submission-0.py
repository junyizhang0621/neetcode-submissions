from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}

        for i in range(len(s)):
            hash_table[s[i]]  = hash_table.get(s[i], 0) + 1
        
        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return i
            
        return -1
