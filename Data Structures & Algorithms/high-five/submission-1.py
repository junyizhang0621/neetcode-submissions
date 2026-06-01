class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        hash_store = {}

        for sid, score in items:
            if sid not in hash_store:
                hash_store[sid] = []
            hash_store[sid].append(-score)
        
        result = []

        for i in hash_store.keys():
            cur_sum = 0
            cur_score = hash_store[i]
            heapq.heapify(cur_score)
            for _ in range(5):
                cur_sum += -heapq.heappop(cur_score)
            result.append([i, int(cur_sum//5)])
        result.sort()
        return result
        