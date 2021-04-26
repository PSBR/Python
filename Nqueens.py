
#Python HW 2
#8 Queens problem (place N queens on an nxn chess board so that none of them could take each other)
#HW2P3Brennan


board = [[0]*8 for _ in range(0,8)]
N = 8

def print_f (board):
    for i in range(N):
        for k in range (N):
            print(board[i][k], end = " ")
        print()

def isSafe (row, col):
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    for j in range(N):
        for k in range(N):
            if (j + k == row + col) or (j - k == row - col):
                if board[j][k] == 1:
                    return False
    return True

def nqueens(n):
    if (n == 0):
        return True
    for i in range(N):
        for j in range(N):
            if isSafe(i,j):
                board[i][j] = 1
                if nqueens(n-1):
                    return True
                board[i][j] = 0
    return False

nqueens(8)
print_f(board)
