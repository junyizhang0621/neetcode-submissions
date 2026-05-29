
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_count = {}

        for i in nums:
            if i in hash_count:
                hash_count[i] += 1
            else:
                hash_count[i] = 1

        count_arr =[[] for _ in range(len(nums))]

        for key, value in hash_count.items():
            count_arr[value-1].append(key)

        result = []

        for i in range(len(count_arr)-1, -1, -1):
            cur_arr = count_arr[i]
            if not cur_arr:
                continue
            
            for c in cur_arr:
                result.append(c)
                k -= 1
                if k == 0:
                    return result



        
       
        
        