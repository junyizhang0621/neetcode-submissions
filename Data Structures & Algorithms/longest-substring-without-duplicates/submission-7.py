class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        hash_table = set()
        result = 0

        i, j = 0, 0

        while j < len(s) and i <= j:
            cur = s[j]
            if cur not in hash_table:
                hash_table.add(cur)
                j+=1
                result = max(result, len(hash_table))
            else:
                hash_table.remove(s[i])
                i+=1
            
        return result



        