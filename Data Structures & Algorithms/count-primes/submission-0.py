class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        res = [True for _ in range(n)]
        res[0] = res[1] = False

        for p in range(2, n):
            if not res[p]:
                continue
            
            for multi in range(p * p, n, p):
                res[multi] = False
        
        return sum(res)