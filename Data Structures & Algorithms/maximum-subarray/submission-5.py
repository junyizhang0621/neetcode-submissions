class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur_sum = nums[0]
        res = nums[0]

        for n in nums[1:]:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += n
            res = max(res, cur_sum)
        
        return res
        