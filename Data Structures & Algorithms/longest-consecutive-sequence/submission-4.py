class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        result = 0

        hashSet = set(nums)

        for i in nums:
            if (i-1) not in hashSet:
                length = 1
                while i + length in hashSet:
                    length += 1
                
                result = max(result, length)
        return result