class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        leftMax, rightMax = height[i], height[j]

        cur_area = 0
        while i < j:
            if leftMax <= rightMax:
                i +=1
                leftMax = max(leftMax, height[i])
                cur_area += leftMax - height[i]
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                cur_area += rightMax - height[j]
        
        return cur_area


        