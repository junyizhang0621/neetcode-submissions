class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        dq = deque()
        i, j = 0, 0

        result = []

        while j < len(nums):
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
            
            dq.append(j)
            
            if j + 1 >= k:
                result.append(nums[dq[0]])
                i += 1
            if i > dq[0]:
                dq.popleft()
            j += 1
        
        return result

    