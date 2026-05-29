class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}

        for i in range(len(nums)):
            hash_table[nums[i]] = i
        
        for i in range(len(nums)):
            check_another = target - nums[i]

            if check_another in hash_table:
                if hash_table[check_another] < i:
                    return [hash_table[check_another], i]
                if hash_table[check_another] > i:
                    return [i, hash_table[check_another]]
                else:
                    continue
        