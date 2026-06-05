class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key =lambda x: x[0])
        
    
        res = []

        for s, e in intervals:
            if not res:
                res.append([s, e])
                continue
            
            prevS, prevE = res[-1]

            if prevE >= s:
                new_intervals = [prevS, max(prevE, e)]
                res.pop()
                res.append(new_intervals)
            else:
                res.append([s, e])
        
        return res


        