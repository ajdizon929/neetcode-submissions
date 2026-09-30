class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Row
        for row in board:
            row_buffer = set()
            for sq in row:
                if sq.isdigit():
                    if sq in row_buffer:
                        print("invalid row")
                        return False
                    else:
                        row_buffer.add(sq)

        # Check Column
        for col in range(9):
            col_buffer = set()
            for row in range(9):
                sq = board[row][col]
                if sq.isdigit():
                    if sq in col_buffer:
                        print("invalid col")
                        return False
                    else:
                        col_buffer.add(sq)

        # Check 3x3 Box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_buffer = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        sq = board[row][col]
                        if sq.isdigit():
                            if sq in box_buffer:
                                print("invalid grid")
                                return False
                            else:
                                box_buffer.add(sq)
        

        return True
        