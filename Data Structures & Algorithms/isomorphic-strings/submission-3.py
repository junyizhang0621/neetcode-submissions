class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        return self.helper(s, t) and self.helper(t, s)

    def helper(self, s, t):
        hash_map = {}
        hash_map2 = {}

        for i in range(len(s)):
            if (s[i] in hash_map and hash_map[s[i]]!= t[i]) or (t[i] in hash_map2 and  hash_map2[t[i]]!=s[i]):
                return False
            hash_map[s[i]] = t[i]
            hash_map2[t[i]] = s[i]
        
        return True
    