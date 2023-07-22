'''
    What if I tell you everything else is the same, But this time I want to traverse in ALL FOUR DIRECTIONS and reach my destination, Give out my paths
    Sounds easy at the beginning, What to do? Just add two more recursion calls , Up and Left , That's it

    Sure kiddo, But lets try to make a recursion tree for that

              _________________________("" , maze , 0 , 0) ____________________
             /                            /            \                       \                       
        ("D" , maze , 1 , 0)  ("R" , maze , 0 , 1)  ("U" , maze , 0 , 0)  ("L" , maze , 0 , 0)

            You see the problem here? Infinite recursion!

    So just simply adding recursive calls won't work, What can we do?

    We can play another smart move and mark the positions we already visited as false, so that our recursion won't visit them again
    BUT wait a second, This is the right way , but it modifies the original maze and that can be a castastrophe for other recursions!
    The other recursions will lose their paths if we do this.

    THIS is the precise moment backtracking walks in:
    Backtracking says "Make changes while traversing through a recursion call , But when you exit, Make sure to revert those changes back"
    In other words, Before a call ends, Make sure to turn all the marks that were false as true and leave the call

    THAT'S IT, THAT IS BACKTRACKING , NO BRO SCIENCE

'''

def backtrackMaze(p , maze , r , c):

    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return [p]
    
    if not maze[r][c]:
        return []

    ans = []

    maze[r][c] = not maze[r][c] # Turning the path for this call as false while we are traversing the maze

    if (r < len(maze) - 1): # Down case
        ans.extend(backtrackMaze(p + 'D' , maze , r + 1 , c))
    
    if (c < len(maze[0]) - 1): # Right case
        ans.extend(backtrackMaze(p + 'R' , maze , r , c + 1))
    
    if (r > 0): # Up case
        ans.extend(backtrackMaze(p + 'U' , maze , r - 1 , c))
    
    if (c > 0): # Left case
        ans.extend(backtrackMaze(p + 'L' , maze , r , c - 1))
    
    # Here, I'll leave the current recursion call and turn the maze back to its original way for other calls to work corectly
    maze[r][c] = not maze[r][c]

    return ans

maze = [
        [1 , 1 , 1],
        [1 , 1 , 1],
        [1 , 1 , 1],
                    ]

print(backtrackMaze("" , maze , 0 , 0))

'''
    Ladies and gentlemen , Backtracking.
'''
    
    
        
