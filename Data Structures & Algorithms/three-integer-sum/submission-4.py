class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            cur_n = nums[i]

            if i != 0 and nums[i] == nums[i-1]:
                continue

            x, y = i + 1, len(nums) - 1

            while x < y:
                cur_sum = cur_n + nums[x] + nums[y]

                if cur_sum == 0:
                    result.append([cur_n, nums[x], nums[y]])
                    x += 1
                    while x < y and nums[x-1] == nums[x]:
                        x += 1
                
                if cur_sum < 0:
                    x += 1
                else:
                    y -= 1
        return result
