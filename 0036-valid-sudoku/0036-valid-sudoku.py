class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # a number must be unique in its row, in its col and in its 3x3 grid
        # we can use a set of string that stores the desc of the number at a cell.
        #  ex: {5 is in row 0, 5 is in col 1, 5 is in grid 0-2}.
        # we dont calculate the actual grid number instead we determine the grids of row index and col index 
        #  and store as string. ex -> i/3 "-"" j/3

        rows = set()
        cols = set()
        grids = set()
        print(2//3)
        print(0//3)
        for i in range(9):
            for j in range(9):
                if(board[i][j] ==  "."):
                    continue
                val = board[i][j]
                cellRow = str(val) + " in row " + str(i)
                cellCol = str(val) + " in col " + str(j)
                cellGrid = str(val) + " in grid " + str(i//3) + "-" + str(j//3)

                if (cellRow in rows) or (cellCol in cols) or (cellGrid in grids):
                    # print(cellRow + " " + cellCol + " " + cellGrid)
                    return False
                else:
                    rows.add(cellRow)
                    cols.add(cellCol)
                    grids.add(cellGrid)

        return True
                    
                