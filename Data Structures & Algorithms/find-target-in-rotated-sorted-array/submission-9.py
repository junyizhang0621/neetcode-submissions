class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1


        while l < r:
            mid = ( l + r)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[r]:
                #pivot is on the right side
                l = mid + 1

            else:
                r = mid
        
        pivot = l

        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            # target is on the right side
            l = pivot
        else:
            # target is the on the left side
            r = pivot - 1
        
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1
        
