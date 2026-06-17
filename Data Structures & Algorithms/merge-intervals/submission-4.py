class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort(key=lambda x: x[0])

        result = []

        for s, e in intervals:
            if not result:
                result.append([s, e])
                continue

            prevS, prevE = result[-1]

            if prevE >= s:
                result.pop()
                result.append([prevS, max(prevE, e)])
            else:
                result.append([s, e])
        
        return result