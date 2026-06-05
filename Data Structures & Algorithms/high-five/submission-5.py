class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        hash_count = {}
        for sid, s in items:
            if sid not in hash_count:
                hash_count[sid] = []
            hash_count[sid].append(-1*s)

        result = []
        for key in hash_count:

            k = 5
            total_score = 0
            #print(hash_count)
            heapq.heapify(hash_count[key])
            for _ in range(k):
                cur_score = heapq.heappop(hash_count[key])
                total_score = total_score + (-1) * cur_score

            avg = total_score//k
            result.append([key, avg])
        result.sort()
        return result

        