# Day & Knight

class Nknights:

    # Logic: Backtracking , Mostly similar to NQueens, But here we eliminate for loops by introducing knights into parameters

    def __init__(self , n):
        self.row = 0
        self.col = 0
        self.board = [[False]*n for _ in range(n)]
        self.knights = n
        self.nknights(self.board , self.row , self.col , self.knights)

    
    def nknights(self , board , row , col , knights):
        if knights == 0:
            self.display(board)
            print("\n")
            return
        
        if row == len(board) - 1 and col == len(board):
            return
        
        if col == len(board):
            self.nknights(board , row + 1, 0 , knights)
            return
        
        if self.isSafe(board , row , col):
            board[row][col] = not board[row][col]
            self.nknights(board , row  , col+1 , knights - 1)
            board[row][col] = not board[row][col]
        
        return self.nknights(board , row , col + 1, knights)
        
    def isSafe(self , board , row , col):
        # What are the moves of a knight?
        if self.isValid(board , row - 2 , col - 1):
            if board[row - 2][col - 1]:
                return False
        if self.isValid(board , row - 2, col + 1):
            if board[row - 2][col + 1]:
                return False
        if self.isValid(board , row - 1 , col - 2):
            if board[row - 1][col - 2]:
                return False
        if self.isValid(board , row - 1 , col + 2):
            if board[row - 1][col + 2]:
                return False
        return True

    
    def isValid(self , board , row , col):
        if row >=0 and row < len(board) and col >=0 and col < len(board[0]):
            return True
        return False

        
    def display(self , board):
        for row in board:
            for element in row:
                if element:
                    print("K ",end='')
                else:
                    print("X ",end='')
            print("\n")
        
Nknights(4)