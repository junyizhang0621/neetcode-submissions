class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}


        i, j = 0, 0
        result = 0

        while j < len(s):

            count[s[j]] = count.get(s[j], 0) + 1

            while (j - i + 1) - max(count.values()) > k:
                 count[s[i]] -= 1
                 i += 1 
            
            result = max(result, j-i + 1)
            j += 1
        
        return result


        