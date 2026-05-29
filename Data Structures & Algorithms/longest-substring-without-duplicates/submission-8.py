
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = set()

        i, j = 0, 0
        
        result = 0
        
        while j < len(s):
            if s[j] not in hash_table:
                hash_table.add(s[j])
                result = max(result, len(hash_table))
                j += 1
            else:
                hash_table.remove(s[i])
                i+=1
        
        return result
        




        