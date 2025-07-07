class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        ### Binary sort 1
        low, high = 0, m - 1
        row_selected = -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row_selected = mid
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        if row_selected == -1:
            return False  # No valid row found

        ### Binary Sort 2
        row = matrix[row_selected]
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        