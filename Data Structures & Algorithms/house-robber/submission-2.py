class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        if len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])

        dp[0] = nums[0]
        dp[1] = nums[1]

        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            dp[i-1] = max(dp[i-1], dp[i-2])

        return max(dp[-1], dp[-2])