class Solution:
    # Logic: Backtracking ; Maze problem (TLE)

    '''
        This is a typical maze problem solved by a backtracking approach

        Nothing difficult, Just realizing that the base case is m == 1 or n == 1
        And return 1 on base case

        After skrimming the whole tree and returning left + right on each recursive call we get the desired answer

        That's it , You get TLE

        This is a bruteforced approach

        Wait for DP ;)

        [4/08/23] DP is here ;)

        Remiscing the words "Those who forget their past are bound to repeat it"

        We'll memoize the solution in DP

        How? It's very easy.
        Start by making a board of m x n consisting of all zeros

        Now the thing to realize is that you can start travelling either from the right of the first cell , Or down the first cell , I mean to say , There is only one way to reach any cell in the first row or column that is by travelling right or bottom , So the first row and first column are set to 1

        Now based on these we can determine different ways to reach each cell in the board

        What are the ways?
        Every other cell can be approached in two ways, Either from the top or from the left , i.e. from top board[i-1][j] and from left [i][j-1] , By filling up the entire matrix with these paths, We end up filling the goal cell with all the unique paths in this manner

        Then? Then we just return the goal cell i.e. return[m-1][n-1]

        That's it, What's so difficult about this? Easy , Cool

    '''
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0]*n for _ in range (m)]

        # Those who forget their past are bound to repeat it

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    board[i][j] = 1
                else:
                    board[i][j] = board[i-1][j] + board[i][j-1]

        return board[m-1][n-1]