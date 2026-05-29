class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)

        for i in range(1, len(nums)):
            left_prod[i] = nums[i - 1] * left_prod[i-1]

        revese_nums = nums[::-1].copy()
        for i in range(1, len(revese_nums)):
            right_prod[i] = revese_nums[i - 1] * right_prod[i-1]
        
        right_prod = right_prod[::-1]

        result = []
        #print(right_prod)
        for i in range(len(nums)):
            result.append(left_prod[i] * right_prod[i])
        
        return result

        