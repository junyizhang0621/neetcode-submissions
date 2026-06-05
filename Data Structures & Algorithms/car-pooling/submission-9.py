class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        cars = [0] * 1001

        for np, s, e in trips:
            cars[s] += np
            cars[e] -= np
        
        check = 0

        for i in cars:
            check += i
            if check > capacity:
                return False
        
        return True
        