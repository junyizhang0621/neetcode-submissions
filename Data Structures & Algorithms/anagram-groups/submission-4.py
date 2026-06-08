class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_count = {}

        for i in strs:
            word_arr = [0] * 26
            for s in i:
                word_arr[ord(s) - ord('a')] += 1

            
            if str(word_arr) not in hash_count:
                hash_count[str(word_arr)] = []
            hash_count[str(word_arr)].append(i)
        
        res = []
        for k in hash_count:
            res.append(hash_count[k])
        
        return res