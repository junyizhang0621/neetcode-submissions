class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
    
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        l, r = 0, len(self.store[key])-1

        result = ""
        while l <= r:
            m = (r + l)//2
            cur_time = self.store[key][m][1]

            if cur_time == timestamp:
                return self.store[key][m][0]
            if cur_time < timestamp:
                result = self.store[key][m][0]
                l = m + 1
            else:
                r = m -1
        
        return result

        
