class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def indexToCoor(i) -> (int, int):
            """
            `i` is already 0-based index, so just return immediately.
            """
            x = i // n
            y = i % n
            return x, y

        l = 0
        r = (m * n) - 1 # treat like 1D array, hence the last index here

        while l <= r:
            mid = int((l+r)/2)
            x, y = indexToCoor(mid)

            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                l = mid + 1
            elif target < matrix[x][y]:
                r = mid - 1
        return False