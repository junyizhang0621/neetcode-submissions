class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0


        l, r = 0, len(height) - 1

        leftMax = []
        cur_left = 0

        for i in range(len(height)):
            cur_left = max(cur_left, height[i])
            leftMax.append(cur_left)
        
        rightMax = []
        cur_right = 0

        for i in range(len(height) - 1, -1, -1):
            cur_right = max(cur_right, height[i])
            rightMax.append(cur_right)
        rightMax = rightMax[::-1]

        for i in range(len(height)):
            cur_vol = max(min(leftMax[i], rightMax[i]) - height[i], 0)
            res += cur_vol
        
        return res
