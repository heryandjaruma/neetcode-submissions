class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # process
        # horizontal and vertical we can just use hash set of n * n

        # 3 separates hashes
        
        horizs = {}
        verts = {}
        squares = {}
        for i, row in enumerate(board):
            for j, square in enumerate(row): # todo skip check if it's dot
                if square == ".":
                    continue
                
                # key = `row#val`
                if f"{i}#{square}" not in horizs:
                    horizs[f"{i}#{square}"] = f"{i}{j}"
                else:
                    return False
                # key = `col#val`
                if f"{j}#{square}" not in verts:
                    verts[f"{j}#{square}"] = f"{i}{j}"
                else:
                    return False
                
                # key = `lsi#val`
                if f"{self.largeSquareIndex(i,j)}#{square}" not in squares:
                    squares[f"{self.largeSquareIndex(i,j)}#{square}"] = f"{i}{j}"
                else:
                    return False
        return True


    # store at max 9 large squares (0-8)
    def largeSquareIndex(self,col, row):
        if (0 <= row <= 2) and (0 <= col <= 2):
            return 0
        if (0 <= row <= 2) and (3 <= col <= 5):
            return 1
        if (0 <= row <= 2) and (6 <= col <= 8):
            return 2
        if (3 <= row <= 5) and (0 <= col <= 2):
            return 3
        if (3 <= row <= 5) and (3 <= col <= 5):
            return 4
        if (3 <= row <= 5) and (6 <= col <= 8):
            return 5
        if (6 <= row <= 8) and (0 <= col <= 2):
            return 6
        if (6 <= row <= 8) and (3 <= col <= 5):
            return 7
        if (6 <= row <= 8) and (6 <= col <= 8):
            return 8

# Time Complexity
# O(n^2)

# Space Complexity
# O(n^2) # TODO verify