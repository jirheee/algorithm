from sys import stdin
import math

def compare(n, m, board):
    # "WBWBWBWB"
    # "BWBWBWBW"
    white_diff = 0
    black_diff = 0
    for i in range(8):
        if i%2==0 and board[n][m+i] == "W":
            black_diff+=1
        if i%2==1 and board[n][m+i] == "B":
            black_diff+=1

        if i%2==0 and board[n][m+i] == "B":
            white_diff+=1
        if i%2==1 and board[n][m+i] == "W":
            white_diff+=1

    return white_diff, black_diff

if __name__ == "__main__":
    n, m = [int(i) for i in stdin.readline().split()]

    board = []

    for _ in range(n):
        board.append(stdin.readline().strip())

    white_diff_list = []
    black_diff_list = []

    for i in range(n):
        white_row = []
        black_row = []
        for j in range(m-7):
            white_diff, black_diff = compare(i, j, board)
            white_row.append(white_diff)
            black_row.append(black_diff)
        white_diff_list.append(white_row)
        black_diff_list.append(black_row)

    minimum = math.inf
    for j in range(m-7):
        for i in range(n-7):
            white_sum = 0
            black_sum = 0
            for k in range(8):
                white_sum += white_diff_list[i+k][j] if k%2==0 else black_diff_list[i+k][j]
                black_sum += black_diff_list[i+k][j] if k%2==0 else white_diff_list[i+k][j]
                
            minimum = min(minimum, min(white_sum, black_sum))
    
    print(minimum)
        
