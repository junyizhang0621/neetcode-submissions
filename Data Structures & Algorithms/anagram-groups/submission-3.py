class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        hash_table = {}

        for s in strs:
            stringKey = [0] * 26
            for c in s:
                stringKey[ord(c) - ord('a')] += 1

            if str(stringKey) not in hash_table:
                hash_table[str(stringKey)] = []
            
            hash_table[str(stringKey)].append(s)
        
        
        for k in hash_table:
            res.append(hash_table[k])
        
        return res