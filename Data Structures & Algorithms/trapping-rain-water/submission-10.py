class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        cur_area = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                cur_area += (leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                cur_area += (rightMax - height[r])
        
        return cur_area

        