# class Solution:
    # # Logic: A Good variant of Maze-Backtracking , CAUSED TLE

    # '''
    #     In maze backtracking our only goal was to make it to the goal while avoiding obstacles, So we started from a fixed cell (0 , 0) and made it to the desired goal cell using backtracking

    #     But what if there is no fixed goal, What if you want to make a target word which starts from anything and ends with anything , You are blindfolded
    #     You have NO IDEA about which cell will contain which element , And the call I'm making to a cell is even valid (in the sense that it should contain the first letter of the target compulsarily) or not. So what would you do in such a situation sherlock?

    #     That's right , You call backtrack on each and every cell of the board , And then the backtrack tries to find if the current backtrack call leads to string formation or not , If any one starting cell returns True, Target is found , Answer is True , Else? We return False

    #     That is the whole logic behind this problem.

    #     Let's look at the backtrack now:
    #         if p == target:
    #             return True
    #         This is very well self explainatory

    #         if row < 0 or col < 0 or row > len(board) - 1 or col > len(board) - 1 or board[row][col] is not in target:
    #             return False
            
    #         If the function breaks any bounds or the cell simply doesn't contain an element from target, Return False

    #         Now I'll trigger the backtrack, REMEMBER THE LINE BELOW FOREVER

    #         temp , board[row][col] = board[row][col] , '#' 

    #         Here I prevent calls to the parent recursion

    #         Then, Start backtracking in all four directions:
    #             found = (self.helper(board , p + temp , target , row + 1 , col) or self.helper(board , p + temp , target , row , col + 1) or self.helper(board , p + temp , target , row - 1 , col) or self.helper(board , p + temp , target , row , col - 1))
            
    #         revert the changes you made before leaving this call
    #         board[row][col] = temp

    #         return found
    #         found is my answer

    #         That's it , Cool
            

    # '''
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     for row in range(len(board)): # Why are we calling the backtracking for every cell?
    #         for col in range(len(board[0])): # Ans : This is different from the maze backtracking where we needed to reach just the goal , In this the word can begin from ANY CELL , So we should backtrack from all cells to consider all possibilities
    #             if self.helper(board , "" , word , row , col):
    #                 return True
    #     return False


    # def helper(self , board , p , target , row , col):
    #     if p == target:
    #         return True
        
    #     if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1 or board[row][col] not in target: # This case handles everything in not entering the obstacle
    #         return False
        
    #     # Triggering backtrack
    #     temp , board[row][col] = board[row][col] , '#' # Imp switching assigning technique, Will help alot in backtracking

    #     found = (self.helper(board , p + temp , target , row + 1 , col) or self.helper(board , p + temp , target , row , col + 1) or self.helper(board , p + temp , target , row - 1 , col) or self.helper(board , p + temp , target , row , col - 1)) # The four directions of backtracking , Answer depens on logical value of found now

    #     #Reverse the change made before leaving the recursive call so as to not affect the answer of other calls
    #     board[row][col] = temp

    #     return found # return the found variable


    # Those who forget their past , Are bound to repeat it. #

class Solution:
    # Logic: Minimalistic DP, Visited memoized the path

    '''
        I'm adding a visited board, Which is marked False initially, And will mark itself True everytime backtrack visits those cells

        The backtrack will fill visited now for its backtracking prevention, Rather than changing the original cell's value

        This will save time , DP is a strong concept fr

        That's it , Done , Everything else same , What's so difficult in this?
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                if self.helper(board, word, "", row, col, visited):
                    return True
        return False
    
    def helper(self, board , target, p , row , col , visited):
        if p == target:
            return True

        if (row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1 or visited[row][col] or board[row][col] != target[len(p)]): # Here I checked for visited , And also to save time I logically checked only the index of target i.e. supposed to be in that cell, Instead of cell in target
            return False

        visited[row][col] = True # Changes are set to this now , The new backtrack condition
        
        found = (self.helper(board, target, p + board[row][col], row + 1, col, visited) or
                 self.helper(board, target, p + board[row][col], row, col + 1, visited) or
                 self.helper(board, target, p + board[row][col], row - 1, col, visited) or
                 self.helper(board, target, p + board[row][col], row, col - 1, visited))

        visited[row][col] = False # Revert the changes before leaving

        return found