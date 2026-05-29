class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_count = {}

        for i in strs:
            cur_count = [0] * 26 

            for c in i:
                cur_count[ord(c) - ord('a')] += 1
            
            cur_count = str(cur_count)
            if cur_count in hash_count:
                hash_count[cur_count].append(i)
            else:
                hash_count[cur_count] = [i]
        
        result = []
        for key, value in hash_count.items():
            result.append(value)
        
        return result