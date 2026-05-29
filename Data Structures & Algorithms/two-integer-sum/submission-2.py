class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}

        for i in range(len(nums)):
            cur_n = nums[i]

            hash_table[cur_n] = i
        
        for i in range(len(nums)):
            check = target - nums[i]

            if check in hash_table and hash_table[check] != i:
                return [i, hash_table[check]]



        