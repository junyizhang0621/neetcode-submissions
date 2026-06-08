class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_store = [[] for i in range(len(nums) + 1)]

        hash_count = {}

        for i in nums:
            hash_count[i] = hash_count.get(i, 0) + 1
        
        for n, freq in hash_count.items():
            freq_store[freq].append(n)

        result = []
    
        for i in range(len(nums), 0,  -1):
            cur_arr = freq_store[i]
            for elem in cur_arr:
                result.append(elem)
                if len(result) == k:
                    return result
        return result