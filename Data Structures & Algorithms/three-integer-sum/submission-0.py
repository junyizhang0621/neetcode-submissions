class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for c in range(len(nums)):
            cur_num = nums[c]
            i = c + 1
            j = len(nums) - 1
            while i < j:
                ln = nums[i]
                rn = nums[j]
                cur_sum =  ln + rn + cur_num

                if cur_sum == 0 and (c != i and c!=j):
                    if [cur_num, ln, rn] not in result:
                        result.append([cur_num, ln, rn])
                    i+=1
                    j -= 1

                
                if cur_sum < 0:
                    i +=1
                if cur_sum > 0:
                    j -= 1
            
        return result


