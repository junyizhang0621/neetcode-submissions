class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hash_table = {}
        count = [[] for _ in range(len(nums) + 1)]


        for i in nums:
            Hash_table[i] = Hash_table.get(i, 0) + 1
        
        result = []

        for elem, freq in Hash_table.items():
            count[freq].append(elem)
        

        for freq in range(len(count) - 1, 0, -1):
            cur_arr = count[freq]
            for elem in cur_arr:
                result.append(elem)
                if len(result) == k:
                    return result