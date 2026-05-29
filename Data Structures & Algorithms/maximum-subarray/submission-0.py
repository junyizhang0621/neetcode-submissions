class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += nums[i]
            maxSum = max(maxSum, cur_sum)
        
        return maxSum