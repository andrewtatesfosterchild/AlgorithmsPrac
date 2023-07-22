def mazePathDiagonal(p , r , c):
    if r == 1 and c == 1: # Base case tells both are one
        return [p] # Append to a list and send p
    
    ans = []

    '''
        Like any other backtracking question, Its just simple DFS nothing else

        Only one case added for diagonal, Everything else is the same

        That's it :/
    '''

    if (r > 1 and c > 1): # Diagonal makes two moves simultaneously i.e. r and c
        ans.extend(mazePathDiagonal(p + 'D' , r - 1 , c - 1))
    if (r > 1):
        ans.extend(mazePathDiagonal(p + 'V' , r - 1 , c))
    if (c > 1):
        ans.extend(mazePathDiagonal(p + 'H' , r , c - 1))
    
    return ans

print(mazePathDiagonal("" , 3 , 3))