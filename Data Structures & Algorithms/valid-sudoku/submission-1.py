class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row_i in range(9):
            for col_i in range(9):
                sq = board[row_i][col_i]
                if sq.isdigit():
                    if ((sq in row[row_i]) or 
                       (sq in col[col_i]) or
                       (sq in squares[(row_i // 3, col_i // 3)])):
                        return False
                    row[row_i].add(sq)
                    col[col_i].add(sq)
                    squares[(row_i // 3, col_i // 3)].add(sq)
        return True
        