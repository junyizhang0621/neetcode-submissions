class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_arr = [[] for i in range(len(nums) + 1)]
        hash_count = {}

        for i in nums:
            hash_count[i] = hash_count.get(i, 0) + 1
        
        for key, c in hash_count.items():
            hash_arr[c].append(key)

        result = []
        for i in range(len(hash_arr)-1, 0, -1):
            for elem in hash_arr[i]:
                result.append(elem)
                if len(result) == k:
                    return result
        return result
        



