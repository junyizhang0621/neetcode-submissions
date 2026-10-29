class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0

        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] <= heights[r]:
                curArea = (r - l) * heights[l]
                res = max(res, curArea)
                l += 1
            else:
                curArea = (r - l) * heights[r]
                res = max(res, curArea)
                r -= 1
        
        return res
        