def mazePath(p , r , c):
    if r == 1 and c == 1: # Base case
        return [p]
    
    ans = []
    
    '''
        Why did you write D condition first and not R condition?
        Anything it is, It is ultimately a DFS approach, Backtracking follows DFS
        Thus, left comes first , Down comes first, ALWAYS

        And this path problem became combination ; It is SAME as the subset problem
        Very easy just the same processed unprocessed approach here too
    '''
    if r > 1:
        ans.extend(mazePath(p + 'D' , r - 1 , c )) 
    if c > 1:
        ans.extend(mazePath(p + 'R' , r , c - 1))

    return ans

print(mazePath("", 3 , 3))