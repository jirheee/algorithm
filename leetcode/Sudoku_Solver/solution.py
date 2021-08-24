from typing import List
from pprint import pprint as pp
from queue import PriorityQueue

class Solution:
    def remove_elem_row(self, row, elem, possibilities):
        for col in range(9):
            try:
                possibilities[row][col].remove(elem)
            except:
                pass

    def remove_elem_col(self, col, elem, possibilities):
        for row in range(9):
            try:
                possibilities[row][col].remove(elem)
            except:
                pass

    def remove_elem_box(self, box_idx, elem, possibilities):
        for i in range(3):
            for j in range(3):
                try:
                    possibilities[3*(box_idx//3)+i][3*(box_idx%3)+j].remove(elem)
                except:
                    pass

    def solveSudoku(self, board: List[List[str]]) -> None:
        possibilities = [[set(range(1,10)) for _ in range(9)] for _ in range(9)]
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem != ".":
                    self.remove_elem_row(i, int(elem), possibilities)
                    self.remove_elem_col(j, int(elem), possibilities)
                    self.remove_elem_box(3*(i//3) + j//3 , int(elem), possibilities)
                    possibilities[i][j] = None
                
        def make_pq():
            pq = PriorityQueue()
            for i in range(9):
                for j in range(9):
                    entry_possibility = possibilities[i][j]
                    if entry_possibility != None:
                        pq.put((len(entry_possibility), (i, j)))
            
            return pq

        pq = make_pq()
        
        while pq.qsize() > 0:
            (l, (i, j)) = pq.get()
            
            candidate = possibilities[i][j].pop()
            board[i][j] = str(candidate)
            
            
            
            self.remove_elem_row(i, candidate, possibilities)
            self.remove_elem_col(j, candidate, possibilities)
            self.remove_elem_box(3*(i//3) + j//3, candidate, possibilities)

            pp(possibilities)

            pq = make_pq()


if __name__ == "__main__":
    board = [
        [".",".","9","7","4","8",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],
        [".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],
        [".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],
        [".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]
    ]

    Solution().solveSudoku(board)

    print(board)

