class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            ln, rn = numbers[l], numbers[r]

            if ln + rn == target:
                return [l+1, r+1]
            if ln + rn > target:
                r -= 1
            else:
                l+= 1
        
    
        