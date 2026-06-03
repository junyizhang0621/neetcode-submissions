class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        heap = []
        cur_cap = 0
        for p, s, d in trips:
            cur_cap += p
            while heap:
                endtime, dropoff = heap[0]
                if s >= endtime:
                    cur_cap -= dropoff
                    heapq.heappop(heap)
                else:
                    break
            if cur_cap > capacity:
                return False
            
            heapq.heappush(heap, (d, p))
        
        return True

            
            
        