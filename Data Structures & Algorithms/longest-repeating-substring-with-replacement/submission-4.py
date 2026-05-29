class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)

        hash_count = {}
        i, j = 0, 1
        hash_count[s[i]] = 1
        result = 0

        maxf = -float('inf')
         
        while j < len(s):
            hash_count[s[j]] = 1 + hash_count.get(s[j], 0)
            maxf = max(maxf, hash_count[s[j]])


            while (j-i+1) - maxf > k:
                hash_count[s[i]] -= 1
                i += 1
        
            result = max(result, j - i + 1)
            j += 1

        return result
                


        