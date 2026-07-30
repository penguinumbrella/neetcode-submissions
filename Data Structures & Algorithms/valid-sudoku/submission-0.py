class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row:
        digits = []
        for row in board:
            #print("row", row)
            for cell in row:
                #print("cell", cell)
                if cell != ".":
                    if cell not in digits:
                        digits.append(cell)
                    else:
                        return False
            #print("digits", digits)
            digits = []
        # col:

        digits = []
        for c in range(0,9):
            #print("row", row)
            for r in range(0,9):
                print("row, col", r,c)
                cell = board[r][c]
                #print("cell", cell)
                if cell != ".":
                    if cell not in digits:
                        digits.append(cell)
                    else:
                        return False
            #print("digits", digits)
            digits = []
        # square:
        digits = []
        for s1 in range(0, 3):
            for s2 in range(0, 3):
                for r in range(0,3):
                    for c in range(0,3):
                        cell = board[s1*3 + r][s2*3 + c]
                        if cell != ".":
                            if cell not in digits:
                                digits.append(cell)
                            else:
                                return False
                digits = []
        return True