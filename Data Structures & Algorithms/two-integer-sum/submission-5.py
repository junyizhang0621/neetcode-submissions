class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_count = {}
        result = []


        for i in range(len(nums)):
            check = target - nums[i]

            if check in hash_count:
                return [hash_count[check], i]
            
            hash_count[nums[i]] = i
        
        return -1
            
