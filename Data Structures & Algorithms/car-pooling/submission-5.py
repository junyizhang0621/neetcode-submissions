class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        
        trips.sort(key=lambda x:x[1])
        minHeap = []
        cur_cap = 0
        for np, s, e in trips[:]:
            while minHeap:
                last_end, last_p = minHeap[0]
                if last_end <= s:
                    cur_cap -= last_p
                    heapq.heappop(minHeap)
                else:
                    break
                
            cur_cap += np
            if cur_cap > capacity:
                return False
        
            heapq.heappush(minHeap, (e, np))

        return True
            



        