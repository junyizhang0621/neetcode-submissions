class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        rightprod = 1
        right_prod_arr = [0] * len(nums)
        leftProd = 1
        left_prod_arr = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                left_prod_arr[0] = 1
            else:
                left_prod_arr[i] = nums[i-1] * left_prod_arr[i-1] 
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                right_prod_arr[i] = 1
            else:
                right_prod_arr[i] = right_prod_arr[i+1] * nums[i+1]


        result = []
        print(left_prod_arr)
        print(right_prod_arr)

        for i in range(len(nums)):
            cur_prod = left_prod_arr[i] * right_prod_arr[i]
            result.append(cur_prod)
        return result
