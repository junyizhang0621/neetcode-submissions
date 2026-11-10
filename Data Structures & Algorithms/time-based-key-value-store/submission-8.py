class TimeMap:

    def __init__(self):

        self.check= {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.check:
            self.check[key] = [(value, timestamp)]
        else:
            self.check[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.check:
            return ''
        cur_arr = self.check[key]
        res = ""
        l, r =0,  len(cur_arr) - 1
        while l <= r:
            mid = (l + r)//2
            v, t = cur_arr[mid]

            if t<= timestamp:
                res = v
                l = mid + 1
            else:
                r = mid-1
        
        return res


