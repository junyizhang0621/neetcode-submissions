class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hash_count = {}
        max_result = 0

        i, j = 0, 0

        while j < len(s):
            lc, rc = s[i], s[j]

            if rc not in hash_count:
                hash_count[rc] = 1
            else:
                hash_count[rc] += 1
                        
            while (j-i+1 )- max(hash_count.values()) > k:
                hash_count[s[i]] -= 1
                i += 1
            max_result = max(max_result, j-i+1)
            j += 1

        return max_result



