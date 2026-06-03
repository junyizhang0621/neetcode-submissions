class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        result = nums[0]
        for i in nums[1:]:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            result = max(result, cur_sum)
        return result
