class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}

        for i in range(len(nums)):
            hash_table[nums[i]]= i


        result = []

        for i in range(len(nums)):
            cur_num = nums[i]
            check = target - cur_num 

            if check in hash_table and i != hash_table[check]:
                return [i, hash_table[check]]


        