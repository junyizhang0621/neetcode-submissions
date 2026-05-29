class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1 :
            return len(s)


        char_count = {}

        i, j = 0, 1

        char_count[s[i]] = 1

        result = 0
        while j < len(s):
            if char_count.get(s[j], 0) == 0:
                char_count[s[j]] = 1
                result = max(result, j - i + 1)
                j += 1
            else:
                char_count[s[i]] = char_count[s[i]] - 1
                i += 1
        
        return result
                



        