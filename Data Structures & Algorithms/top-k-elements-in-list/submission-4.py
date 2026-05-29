class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_count = [[] for _ in range(len(nums))]

        hash_table = {}
        for i in nums:
            hash_table[i] = hash_table.get(i, 0) + 1
        
        print(hash_table)

        for key, val in hash_table.items():
            hash_count[val-1].append(key)
        
        result = []
        #print(hash_count)
        for i in range(len(hash_count) - 1, -1, -1):
            result += hash_count[i]
            #print(result)
            if len(result) == k:
                return result
        
        return result


        