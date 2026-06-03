class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        heap = []
        Hash_table = {}
        result = []


        for sid, score in items:
            if sid not in Hash_table:
                Hash_table[sid] = []
                heapq.heappush(Hash_table[sid], -score)
            else:
                heapq.heappush(Hash_table[sid], -score)
        
        for key in Hash_table:
            k = 5
            cur_sum = 0
            for _ in range(k):
                cur_sum += -1 * heapq.heappop(Hash_table[key])
            
            cur_avg = cur_sum//k
            result.append([key, cur_avg])

        result.sort(key = lambda x: x[0])
        return result        