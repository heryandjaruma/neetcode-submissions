class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # The challenge is how to traverse properly

        m = len(matrix)
        n = len(matrix[0])

        # find potential row
        l = 0
        r = m - 1
        potentialRow = None
        while l <= r:
            midRow = int((l + r) / 2)
            if matrix[midRow][0] <= target and matrix[midRow][n-1] >= target:
                potentialRow = midRow
                break
            elif target < matrix[midRow][0]:
                r = midRow -1
            elif target > matrix[midRow][n-1]:
                l = midRow + 1
        if potentialRow:
            return False
        

        # then do regular binary search
        l = 0
        r = n - 1
        row = matrix[potentialRow]
        while l <= r:
            midCol = int((l + r) / 2)
            if target == row[midCol]:
                return True
            elif target < midCol:
                r = midCol
            elif target > midCol:
                l = midCol
        return False