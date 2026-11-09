class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        l, r = 1, max(piles)
    
        res = float('inf')
        while l <= r:
            speed = (l + r)//2
            cur_time = 0

            for p in piles:
                t = -(-p // speed)
                cur_time += t
                if cur_time > h:
                    l = speed + 1
                    break
            
            if cur_time <= h:
                r = speed - 1
                res = min(res, speed)
        
        return res



        