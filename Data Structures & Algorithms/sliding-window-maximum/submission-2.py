class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        
        cur_max = max(nums[:k])
        result = [cur_max]

        hash_count = {}

        for i in range(k):
            hash_count[nums[i]] =  hash_count.get(nums[i], 0) + 1

        l = 0
        for r in range(k, len(nums)):
            hash_count[nums[l]] -= 1
            l += 1
            hash_count[nums[r]] = hash_count.get(nums[r], 0) + 1
            if nums[r] <= cur_max and hash_count[cur_max] != 0:
                result.append(cur_max)
            elif nums[r] <= cur_max and hash_count[cur_max] == 0:
                cur_max= -float('inf')
                for c in hash_count:
                    if hash_count[c] != 0:
                        cur_max = max(cur_max, c)
                result.append(cur_max)
            elif nums[r] > cur_max:
                 cur_max = nums[r]
                 result.append(cur_max)
        
        return result


        