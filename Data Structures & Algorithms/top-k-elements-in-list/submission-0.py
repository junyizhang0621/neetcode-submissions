class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_hash = {}
        for i in nums:
            if i in count_hash:
                count_hash[i] += 1
            else:
                count_hash[i] = 1
            

        arr = []
        for elem, count in count_hash.items():
            arr.append([count, elem])
        
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result
        
        