class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in board:
            row_set = set()
            for x in row:
                if x == ".":
                    continue
                if x in row_set:
                    return False
                row_set.add(x)

        # Check columns
        for col in range(len(board[0])):
            col_set = set()
            for row in board:
                y = row[col]
                if y == ".":
                    continue
                if y in col_set:
                    return False
                col_set.add(y)

        # Check 3x3 grids
        grid_center_squares = {
            (1, 1),
            (1, 4),
            (1, 7),
            (4, 1),
            (4, 4),
            (4, 7),
            (7, 1),
            (7, 4),
            (7, 7),
        }

        for row, col in grid_center_squares:
            # [x - 1][y - 1], [x - 1][y], [x - 1][y + 1]
            # [x][y - 1], [x][y], [x][y + 1]
            # [x + 1][y - 1], [x + 1][y], [x + 1][y + 1]
            inner_grid_set = set()
            for x in range(-1, 2):
                for y in range(-1, 2):
                    el = board[row + x][col + y] # [1 - 0, 1 - 0]
                    if el == '.':
                        continue
                    if el in inner_grid_set:
                        return False
                    inner_grid_set.add(el)
        
        return True



# I keep forgetting about tuples T_T
