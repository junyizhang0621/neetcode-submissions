class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        targetSum = k * threshold

        l, r = 0, k
        cur_sum = sum(arr[l:r])

        count = 0 if cur_sum < targetSum else 1

        while r < len(arr):
            cur_sum = cur_sum + arr[r] - arr[l]
            if cur_sum >= targetSum:
                count += 1
            
            r+=1
            l+=1
        
        return count

