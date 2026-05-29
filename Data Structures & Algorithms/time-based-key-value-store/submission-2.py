class TimeMap:

    def __init__(self):
        self.hash_table = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_table:
            self.hash_table[key] =[(value, timestamp)]
        else:
            self.hash_table[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        if key not in self.hash_table:
            return result

        value_arr = self.hash_table[key]

        l, r = 0, len(value_arr) - 1

        while l <= r:
            mid = (r + l)//2
            v, t = value_arr[mid]

            if t <= timestamp:
                result = v
                l = mid + 1
            else:
                r = mid-1
        return result
        
