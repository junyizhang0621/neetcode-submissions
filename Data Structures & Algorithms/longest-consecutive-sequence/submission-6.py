class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        hash_set = set(nums)
        
        count = 1

        for i in nums:
            cur_lenght = 1
            while i + cur_lenght in hash_set:
                cur_lenght += 1
            
            count = max(count, cur_lenght)
        
        return count
