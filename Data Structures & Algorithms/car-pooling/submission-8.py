class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])

        p, s, e = trips[0]
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (e, p))

        curP = p
        if curP > capacity:
            return False

        for newP, newS, newE in trips[1:]:
            while heap:
                latestE, latestP = heap[0]
                if newS >= latestE:
                    curP -= latestP
                    heapq.heappop(heap)
                else:
                    break
                    
            curP += newP
            if curP > capacity:
                return False
            
            heapq.heappush(heap, (newE, newP))
        
        return True
