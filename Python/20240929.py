import random
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def validate(board):
            
            def is_unit_valid(unit):
                unit = [i for i in unit if i != '.']
                return len(set(unit)) == len(unit)
            
            def is_row_validate(board):
                for row in board:
                    if not is_unit_valid(row):
                        return False
                return True
            
            def is_col_validate(board):
                for col in zip(*board):
                    if not is_unit_valid(col):
                        return False
                return True
            
            def is_sub_validate(board):
                for i in range(0,7,3):
                    for j in range(0,7,3):
                        unit = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                        if not is_unit_valid(unit):
                            return False
                return True
            
            return is_row_validate(board) and is_col_validate(board) and is_sub_validate(board)

        invalid = set()
        # initialization
        candidate = []
        for line in board:
            c = [str(i) for i in range(1,10)]
            e = [i for i in line if i != '.']
            result = [item for item in c if item not in e]
            candidate.append(result)
        count = 0
        while True:
            print(count)
            count += 1
            candidate_board = []
            for i in range(9):
                candidate_board.append([])
                index = 0
                for j in range(9):
                    if board[i][j] != '.':
                        candidate_board[i].append(board[i][j])
                    else:
                        candidate_board[i].append(candidate[i][index])
                        index += 1
            candidate_tuple = tuple(tuple(row) for row in candidate_board)
            if candidate_tuple not in invalid and validate(candidate_board):
                board = candidate_board
                break
            else:
                if candidate_tuple not in invalid:
                    invalid.add(candidate_tuple)
                for line in candidate:
                    length = len(line)
                    for _ in range(random.randint(0,length//3)):
                        p1 = random.randint(0,length-1)
                        p2 = random.randint(0,length-1)
                        line[p1], line[p2] = line[p2], line[p1]


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
print(board)

