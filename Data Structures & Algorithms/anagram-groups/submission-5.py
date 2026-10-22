class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        string_hash = {}

        for w in strs:
            char_hash = [0] * 26

            for c in w:
                char_hash[ord(c) - ord('a')] += 1

            if str(char_hash) in string_hash:
                string_hash[str(char_hash)].append(w)
            else:
                string_hash[str(char_hash)] = [w]
        
        result = []
        for key in string_hash:
            result.append(string_hash[key])
        return result