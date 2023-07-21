def mazeCount(r , c):
    if r == 1 or c == 1: # Base case
        return 1
    
    left = mazeCount(r - 1 , c)
    right = mazeCount(r , c- 1)

    return left + right

print(mazeCount(3 , 3))