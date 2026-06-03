class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for s, end in intervals[1:]:
            lastS, lastEnd = result[-1]

            if s <= lastEnd:
                newEnd = max(lastEnd, end)
                result[-1] = [lastS, newEnd]
            else:
                result.append([s, end])
        
        return result



        