class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)

        hash_count = set(nums)

        result = 1

        for i in nums:
            length = 1
            while i + length in hash_count:
                length += 1
                result = max(result, length)

        
        return result

        