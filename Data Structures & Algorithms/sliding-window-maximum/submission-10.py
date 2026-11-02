class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidates = deque()

        l, r = 0, 0
        
        res = []
        
        while r < len(nums):
            while candidates and candidates[0] <= r - k:
                candidates.popleft()
            
            while candidates and nums[candidates[-1]] <= nums[r]:
                candidates.pop()
            
            candidates.append(r)

            if r >= k - 1:
                res.append(nums[candidates[0]])
            r+= 1
        
        return res