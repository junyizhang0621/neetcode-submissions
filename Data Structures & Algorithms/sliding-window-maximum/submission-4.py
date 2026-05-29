class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        l = r = 0

        while r < len(nums):

            # if leftmost value (which is current max value) is less than new value
            # pop until the new max value so that top of the index is always max
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                result.append(nums[q[0]])
                l += 1
            r+=1
        
        return result




        