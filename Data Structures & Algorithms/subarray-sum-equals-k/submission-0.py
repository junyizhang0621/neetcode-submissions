class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        
        count = {0:1}

        for i in nums:
            curSum += i
            if curSum - k in count:
                res += count[curSum - k]
                count[curSum] = count.get(curSum, 0) + 1
            else:
                count[curSum] = count.get(curSum, 0) + 1
            
        return res