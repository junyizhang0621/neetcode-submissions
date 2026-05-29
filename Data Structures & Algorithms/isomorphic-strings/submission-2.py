class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        return self.helper(s, t) and self.helper(t, s)

    def helper(self, s, t):
        hash_map = {}

        for i in range(len(s)):
            if s[i] in hash_map and hash_map[s[i]] != t[i]:
                return False
            hash_map[s[i]] = t[i]
        
        return True
    