class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        target = k * threshold

        if len(arr) < k:
            return 0

        i, j = 0, k -1

        cur_sum = sum(arr[:k])
        count = 0
        if cur_sum >= target:
            count = 1
        
        while j < len(arr) - 1:
            cur_sum -= arr[i]
            i += 1
            j += 1
            cur_sum += arr[j]
            if cur_sum >= target:
                count += 1

        return count
        