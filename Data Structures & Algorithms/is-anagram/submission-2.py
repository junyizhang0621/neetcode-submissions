class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_count_1 = {}
        char_count_2 = {}

        for c in s:
            char_count_1[ord(c) - ord('a')] = char_count_1.get(ord(c) - ord('a'), 0) + 1
        
        for c in t:
            char_count_2[ord(c) - ord('a')] = char_count_2.get(ord(c) - ord('a'), 0) + 1
        
        return char_count_1 == char_count_2

        