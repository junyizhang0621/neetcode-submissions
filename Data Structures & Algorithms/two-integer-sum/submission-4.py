class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}
        check = set(nums)
        
        for i in range(len(nums)):
            hash_table[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in check and i != hash_table[diff]:
                return [i, hash_table[diff]]
            
            

        