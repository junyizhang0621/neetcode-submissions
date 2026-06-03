class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])

        result = []

        for s, e in intervals:
            if not result:
                result.append([s, e])
                continue
            lastS, lastE = result[-1]
            if lastE < s:
                result.append([s, e])
            else:
                result.pop()
                result.append([lastS, max(lastE, e)])
        
        return result

        