class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_set = {}

        for i in nums:
            if i not in hash_set:
                hash_set[i] = 1

            else:
                return True
        
        return False
        