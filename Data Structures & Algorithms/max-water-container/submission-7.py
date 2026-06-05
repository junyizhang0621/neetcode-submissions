class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0
        i, j = 0, len(heights) - 1

        while i < j:
            if heights[i] <= heights[j]:
                cur_area = (j - i) * heights[i]
                result = max(result, cur_area)
                i +=1
            else:
                cur_area = (j - i) * heights[j]
                result = max(result, cur_area)
                j -=1
        
        return result

        