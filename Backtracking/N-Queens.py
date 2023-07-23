# You must take your opponent off a deep down road where 2 + 2 = 5 , And the way out is only wide enough for one
# ~ Mikhail tal
# This is my tribute to Tal , My master

class Nqueens:

    def __init__(self , n):
        self.row = 0
        self.col = 0
        self.board = [([False]*n) for _ in range(n)]
        print(self.queens(self.board , self.row))


    def queens(self , board , row):
        if row == len(board):
            self.display(board)
            print("\n")
            return 1

        
        count = 0
        # Placing the queen and checking for rows and columns
        for col in range(len(board)):
            if self.isSafe(board , row , col):
                board[row][col] = True # Backtracking triggered
                count = count + self.queens(board , row + 1)
                board[row][col] = not board[row][col] # Changing it back to the way it ways at the end of call , For not disturbing the other calls

        return count


    def isSafe(self , board, row, col):
        # Vertical row check
        for i in range(row):
            if board[i][col]: # There's already a queen on ths vertical row
                return False
        
        # Diagonal left check
        maxLeft = min(row , col) # Think about it, If I have to move left on a chess board, I can go max about the minimum of row or col, Since we ate moving idagonally and both will decrement together
        
        for i in range(1 , maxLeft+1): # start by subtracting one , till the maxleft to check all left diagonal squares
            if board[row - i][col - i]: # There's already a queen threatening this diagonal
                return False
        
        # Diagonal right check
        maxRight = min(row , len(board) - col - 1) # Why minimum , I already explained if you go max the other will decrease and go beyond the chessboard
        '''
                            -------------------   -> Board
                                   Q
                                  col --------- -> len(board) - col - 1 (This area) -1 to exclude the current element square
        '''

        for i in range(1 , maxRight + 1):
            if board[row - i][col + i]: # There's already a queen on this diagonal
                return False
            
        return True # Queen can be placed, Passed all checks




    def display(self , board):
        for row in board:
            for element in row:
                if element:
                    print("Q " , end="")
                else:
                    print("X " , end="")
            print()

Nqueens(5)