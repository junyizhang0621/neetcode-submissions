class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_count1 = {}
        hash_count2 = {}

        for i in s:
            hash_count1[i] = hash_count1.get(i, 0) + 1
        
        for i in t:
            hash_count2[i] = hash_count2.get(i, 0) + 1


        return hash_count1 == hash_count2        