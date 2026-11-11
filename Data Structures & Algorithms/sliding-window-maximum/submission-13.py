class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidates = deque()

        res = []

        for i in range(len(nums)):
            while candidates and candidates[0] <= i -k:
                candidates.popleft()
            
            while candidates and nums[candidates[-1]] <= nums[i]:
                candidates.pop()

            candidates.append(i)

            if i - k + 1 >= 0:
                res.append(nums[candidates[0]])
        
        return res
