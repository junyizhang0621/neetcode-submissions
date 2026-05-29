class Solution:
    def trap(self, height: List[int]) -> int:

        left_max, right_max = -float('inf'), -float('inf')

        left_h, right_h = [], []

        for i in range(len(height)):
            left_max = max(height[i], left_max)
            left_h.append(left_max)

        for i in range(len(height) - 1, -1,-1):
            right_max = max(height[i], right_max)
            right_h.append(right_max)

        right_h = right_h[::-1]

        result = 0

        for i in range(len(height)):
            cur_area = min(left_h[i], right_h[i]) - height[i]
            result += cur_area

        return result
            
            
        