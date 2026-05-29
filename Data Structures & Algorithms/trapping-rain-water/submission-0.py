class Solution:
    def trap(self, height: List[int]) -> int:

        leftMin = 0
        rightMin = 0

        left_arr = []
        right_arr = []

        for i in range(len(height)):
            cur = height[i]
            leftMin = max(cur, leftMin)
            left_arr.append(leftMin)
        
        for i in range(len(height)-1, -1, -1):
            cur = height[i]
            rightMin = max(cur, rightMin)
            right_arr.append(rightMin)
        
        right_arr = right_arr[::-1]

        total = 0
        i, j = 0, len(height) - 1

        for i in range(len(height)):
            cur = max(min(right_arr[i], left_arr[i]) - height[i], 0)
            total += cur
        
        return total
            
        