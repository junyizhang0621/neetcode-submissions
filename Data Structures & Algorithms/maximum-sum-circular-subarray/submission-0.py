class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0,0
        bestMax, bestMin = nums[0], nums[0]
        total = 0
        for i in nums:
            total += i
            curMax = max(i, curMax+i)
            curMin = min(i, curMin+i)
            bestMax = max(bestMax,curMax)
            bestMin = min(bestMin, curMin)

        return max(bestMax, total-bestMin) if bestMax > 0 else bestMax