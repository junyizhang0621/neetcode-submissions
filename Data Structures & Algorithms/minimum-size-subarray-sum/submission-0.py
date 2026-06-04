class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = float('inf')

        l, r = 0, 0
        cur_sum = 0
        while r < len(nums) and l <= r:
            cur_sum += nums[r]
            while cur_sum >= target:
                res = min(res, (r - l + 1))
                cur_sum -= nums[l]
                l += 1
            else:
                r += 1
        
        if res == float('inf'):
            return 0
        return res

            
