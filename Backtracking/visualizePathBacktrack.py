def visualizePath(p , r , c , path , step):
    if r == len(board) - 1 and c == len(board[0]) - 1:
       path[r][c] = step # Reaching goal is also a step
       for row in path:
           print (row)
       print (p, end="\n")
        
    if not board[r][c]:
        return
        
    board[r][c] = not board[r][c] # Backtrack start
    path[r][c] = step

    if r < len(board) - 1: # Case Down
        visualizePath(p + 'D' , r + 1 , c , path , step + 1) # Step increments on every call
    if c < len(board[0]) - 1: # case Right
        visualizePath(p + 'R' , r , c + 1 , path , step + 1)
    if r > 0: # case Up
        visualizePath(p + 'U' , r - 1 , c , path , step + 1)
    if c > 0: # case Left
        visualizePath(p + 'L' , r , c - 1 , path , step + 1)
    
    # Here I'm leaving the recursion call, I'll reset the board and path for other calls

    board[r][c] = not board[r][c]
    path[r][c] = 0


board = [[1 , 1 , 1], [1 , 1 , 1], [1 , 1 , 1]] # Many references pointing at one object
path = [[0 , 0 , 0] , [0 , 0 , 0] , [0 , 0 , 0]] # Many references pointing at one object
visualizePath("" , 0 , 0 , path , 1)

