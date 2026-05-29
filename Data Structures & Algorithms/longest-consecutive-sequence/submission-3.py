class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        min_num = min(nums)
        max_num = max(nums)

        longest_series = 0
        cur_length = 1

        hash_set = set(nums)

        while min_num <= max_num:
            min_num += 1
            if min_num in hash_set:
                cur_length += 1
            else:
                longest_series = max(cur_length, longest_series)
                cur_length = 0
        
        return longest_series