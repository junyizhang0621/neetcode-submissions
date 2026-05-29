class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque will store indices of elements
        # Values are kept in decreasing order (largest at the front)
        window = deque()

        result = []
        left = 0   # left pointer of window

        for right in range(len(nums)):

            # 1. Remove all smaller elements from the back
            # because they can never be maximum
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            # 2. Add current index
            window.append(right)

            # 3. Remove indices that are outside the window
            if window[0] < right - k + 1:
                window.popleft()

            # 4. When window size reaches k, record the max
            if right >= k - 1:
                result.append(nums[window[0]])

        return result
    