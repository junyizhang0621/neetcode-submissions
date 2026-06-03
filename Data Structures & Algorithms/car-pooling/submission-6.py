class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car_arr = [0] * 1001

        for np, s, end in trips:
            car_arr[s] += np
            car_arr[end] -= np
        
        cur = 0
        for i in car_arr:
            cur += i
            if cur > capacity:
                return False
        return True
