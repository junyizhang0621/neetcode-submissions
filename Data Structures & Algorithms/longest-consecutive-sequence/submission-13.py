class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        check_hash = set(nums)

        result = 1

        for i in nums:
            if i - 1 not in check_hash:
                l = 1
                while i + l in check_hash and l < len(nums):
                    l += 1
                result = max(result, l)
        
        return result
