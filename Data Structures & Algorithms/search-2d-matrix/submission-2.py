class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_l, row_r = 0, len(matrix) - 1

        while row_l <= row_r:
            mid = (row_l + row_r)//2
            cur_r = matrix[mid]

            cur_max, cur_min = cur_r[-1], cur_r[0]

            if cur_min <= target <= cur_max:
                return self.binary(cur_r, target)
            if target > cur_max:
                row_l += 1
            else:
                row_r -= 1
        return False
    
    def binary(self, arr, target):
        l, r = 0, len(arr)

        while l < r:
            mid = (r + l)//2

            if arr[mid] == target:
                return True
            if arr[mid] > target:
                r -= 1
            else:
                l += 1
        return False

       
