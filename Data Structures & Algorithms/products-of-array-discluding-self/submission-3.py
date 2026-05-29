class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]
        after = [1]

        cur_sum = 1
        for i in range(len(nums) - 1):
            cur_sum = cur_sum * nums[i]
            pre.append(cur_sum)


        cur_sum = 1
        for i in range(len(nums) - 1, 0, -1):
            cur_sum = cur_sum * nums[i]
            after.append(cur_sum)
        after = after[::-1]

        result = []
        for i in range(len(nums)):
            result.append(pre[i] * after[i])
        
        return result