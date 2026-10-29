class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0

        l, r = 0, len(height) - 1

        leftMax, rightMax = height[l], height[r]

        while l < r:
            if height[l] <= height[r]:
                leftMax = max(leftMax, height[l])
                cur_area = max(0, leftMax - height[l])
                total += cur_area
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                cur_area = max(0, rightMax - height[r])
                total += cur_area
                r -= 1
        
        return total
        