class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j = 0, len(heights) - 1

        maxWater = 0

        while i < j:
            leftH = heights[i]
            rightH = heights[j]
            curWater = min(leftH, rightH) * (j-i)
            maxWater = max(maxWater, curWater)

            if leftH < rightH:
                i += 1
            elif leftH >= rightH:
                j -= 1
        
        return maxWater

        

