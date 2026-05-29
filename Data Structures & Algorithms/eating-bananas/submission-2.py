
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        result = r
        while l <= r:
            mid = max((r + l)//2, 1)
            cur_time = sum([math.ceil(i / mid) for i in piles])
            #print([math.ceil(i / mid) for i in piles])
            #print(cur_time)
            if cur_time <= h:
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return result

        


        