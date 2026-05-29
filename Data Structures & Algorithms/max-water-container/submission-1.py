class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        leftMax = []
        rigthtMax = []

        left_max = 0
        for i in heights:
            left_max = max(i, left_max)
            leftMax.append(left_max)


        rigtht_max = 0
        for i in range(len(heights) - 1, -1, -1):
            right_max = max(heights[i], rigtht_max)
            rigthtMax.append(right_max)
        
        rigthtMax = rigthtMax[::-1]

        i, j = 0, len(heights) - 1

        maxWater = 0

        while i < j:
            leftH = leftMax[i]
            rightH = rigthtMax[j]
            curWater = min(leftH, rightH) * (j-i)
            maxWater = max(maxWater, curWater)

            if leftH < rightH:
                i += 1
            elif leftH >= rightH:
                j -= 1
        
        return maxWater

        

