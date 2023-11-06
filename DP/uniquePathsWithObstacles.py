class Solution:
    # Logic: Backtracking on a maze ; Visited Memoization failed - DP to the rescue



    # I'll keep the original approcah you've used untouched , So you know the beauty of your approach

    '''
        The recursive memoization was indeed excellent but gave a TLE

        So walks in DP

        The DP for this question too is very similar and easy.

        Only some conditions are different rest everything is same
        And what has changed is totally logical

        Wanna see?
        Firstly, What if there is a big rock blocking all the paths in front of you while starting the trip, You wont be able to traverse, so return 0

        Can I walk through walls? No right? So can I walk through rocks? Definitely NO
        So how will board[row][0] or board[0][col] will be in the path if the path before it was blocked by a rock? Or worse if board[row][0] or board[0][col] itself has a rock blocking further paths, So the setting of such cells depends on the boolean of the previous two conditions

        Similarly while the rest of the grid traversal, if the cell encountered is a rock, Turn that cell into 0 and keep moving, indicating no further paths from that cell to the goal

        That's it, Was this so tough? how many times have I done this same question so far?
        Cool


    '''
    def uniquePathsWithObstacles(self, board: List[List[int]]) -> int:
        if board[0][0] == 1: # Start is an obstacle
            return 0
        ##################### Old code #####################
        # visited = [[False]*len(obstacleGrid[0]) for x in range (len(obstacleGrid))]
        # return (self.helper("" , obstacleGrid , 0 , 0 , visited))
        ##################### Old code #####################

        board[0][0] = 1 # For populating

        # Cell should itself not be an obstacle, And the previous cell too must not be an obstacle, i.e. it should have a path == 1
        # But wont it mean that prev cell is an obstacle?
        #Aree What kind of question is this? We are traversing serially over all cells, how can It be an obstacle if it itself has been checked before?

        for row in range(1 , len(board)):
            board[row][0] = int(board[row-1][0] == 1 and board[row][0] == 0)
        for col in range(1 , len(board[0])):
            board[0][col] = int(board[0][col-1] == 1 and board[0][col] == 0)

        for row in range(1 , len(board)):
            for col in range(1 , len(board[0])):
                if board[row][col]:
                    board[row][col] = 0
                else:
                    board[row][col] = board[row - 1][col] + board[row][col - 1]

        return board[-1][-1]
    
    #################### Old Code ####################
    
    # def helper(self , p , board  , row , col , visited):
    #     if row == len(board) - 1 and col == len(board[0]) - 1:
    #         return 1
        

    #     if board[row][col] == 1 or visited[row][col] == True:
    #         return 0

    #     #start backtracking
    #     count = 0
    #     visited[row][col] = True

    #     if col < len(board[0]) - 1:
    #         count = count + (self.helper(p + 'R' , board , row , col + 1 , visited))
        
    #     if row < len(board) - 1:
    #         count = count + (self.helper(p + 'D' , board , row + 1 , col , visited))
        
    #     visited[row][col] = False

    #     return count

    #################### Old Code ####################