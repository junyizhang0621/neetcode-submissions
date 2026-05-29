class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        result = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                h, index = stack.pop()
                result = max(result, (i-index) * h)
                start = index
            
            stack.append((heights[i], start))
        
        for h, index in stack:
            result = max(result, h * (len(heights) - index))
        
        return result

        


        