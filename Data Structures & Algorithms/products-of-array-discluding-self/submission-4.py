class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums) - 1):
            left[i+1] = left[i] * nums[i] 
            # [1, 1, 2, 8]
        
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = right[i] * nums[i]
            # [48, 24, 6, 1]

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result
        