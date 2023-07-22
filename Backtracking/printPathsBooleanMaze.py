def booleanMaze(maze , p , r , c):
    '''Nothing has changed here,
        Just we have to traverse the matrix with recursion THAT's IT.
        EVERYTHING ELSE IS SAME, Just the constrains and logical parts have changed rest all is SAME
        lame questions -_-'''
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return [p]
    
    ans = []
    
    if not maze[r][c]:
        return [] # Kill the recursion in river, Return an empty list here instead of Nothing
    '''
        But why empty list has to be returned, why not just do return?
        Because, see the recursion. It extends the main ans with the paths received from below calls.
        Can't extend a list with Nonetype, That's it, That's the reason
    '''
    if r < len(maze) - 1:
        ans.extend(booleanMaze(maze , p + 'D' , r + 1 , c))
    if c < len(maze[0]) - 1:
        ans.extend(booleanMaze(maze , p + 'R' , r , c + 1))
    
    return ans


maze = [
        [1 , 1 , 1],
        [1 , 0 , 1],
        [1 , 1 , 1]
                    ]
print (booleanMaze(maze , "" ,  0 , 0))