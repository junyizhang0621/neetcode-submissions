class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        result = []

        i = 0
        j = len(numbers) - 1

        while i <= j:
            ln = numbers[i]
            rn = numbers[j]
    
            cur_sum = ln + rn
            if cur_sum == target and i != j:
                return [i+1, j+1]
            
            if cur_sum > target:
                j -=1
            else:
                i +=1

        