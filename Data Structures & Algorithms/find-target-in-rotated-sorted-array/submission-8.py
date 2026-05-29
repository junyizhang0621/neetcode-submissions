class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1


        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Case 1: left half [l..mid] is sorted
            if nums[l] <= nums[mid]:
                # target is inside the sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Case 2: right half [mid..r] is sorted
            else:
                # target is inside the sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
        