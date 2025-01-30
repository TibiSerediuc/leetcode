class Solution:
    """
    Time complexity:  O(log(m*n))
    Space complexity: O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #basically we all elements in the matrix as contiguous in memory and apply the binary search algorith
        #only when we have to access the elements by line and column index we have to find the right element
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False