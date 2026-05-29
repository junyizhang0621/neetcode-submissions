class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0
        x, y = 0, len(height) - 1
        left = 0
        right = 0

        while x < y:
            cur_l = height[x]
            cur_r = height[y]


            left = max(left, cur_l)
            right = max(right, cur_r)


            if left <= right:
                total += max(min(left, right) - cur_l, 0)
                x+=1
            else:
                total += max(min(left, right) - cur_r, 0)
                y-= 1
                
        return total

            
        