class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # every element in the list row is distinct
        # every element in the list with the same index is distinct
        # every element with 0-2, 3-5, 6-8 index is distinct



        for row in board:
            hash_row = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for tile in row:
                if tile.isnumeric():
                    if hash_row[int(tile)] == 0:
                        hash_row[int(tile)] += 1
                    else:
                        return False
                elif tile == ".":
                    continue
                else:
                    return False

        index_col = 0

        while index_col < 9:
            hash_col = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for row in board:
                if row[index_col].isnumeric():
                    if hash_col[int(row[index_col])] == 0:
                        hash_col[int(row[index_col])] += 1
                    else:
                        return False

                elif row[index_col] == ".":
                    continue


            index_col += 1

        for start_row_s in range(0, 7, 3):
            for start_col_s in range(0, 7, 3):
                hash_sqr = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
                for row_s in range(start_row_s, start_row_s+3):
                    for col_s in range(start_col_s, start_col_s+3):
                        print(board[row_s][col_s])
                        print(hash_sqr)
                        if board[row_s][col_s].isnumeric():
                            if hash_sqr[int(board[row_s][col_s])] == 0:
                                hash_sqr[int(board[row_s][col_s])] += 1
                            else:
                                return False

                        elif board[row_s][col_s] == ".":
                            continue
                            
                        print(row_s, col_s)



        return True

        print(hash_row)
                    

