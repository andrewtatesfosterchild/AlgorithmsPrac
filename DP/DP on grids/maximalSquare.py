class Solution:
    #Logic: Classic DP on grids

    '''
        What's the primary intuition after seeing a DP on grids problem?
        I have to optimize the goal cell by using surrounding cells

        That is correct. Totally right.

        Now, Think of it this way, There is not one goal cell,
        But we'll have a goal cell on every square check of 2*2
        Where will this goal cell be? At the bottom right corner of every 2*2 square

        But wait, Why a 2*2 square?
        1*1 means a cell, There's no dimensions to check for that
        So 2*2 becomes our smallest problem to solve in this question

        Take the wise words from a man:
        Always look for smaller , smaller , smallest problems while solving a DP question,
        Solve those and the solution unweils itself.

        Coming back , a 2*2 square, Now what sherlock -_-,
        Now, We do the same thing as we do in every DP on grid, check above and check left,
        Since there are two ways of reaching the current cell

        One cleverness we'll do here and the question is over, There and there.

        Whenever a 0 occurs I know the link breaks and the square falls apart,
        But when I have three ones in a four ones in a square, i.e. when I'm checking a cell,
        And I see a presence of 1, (why would I check 0 when I know 0 breaks links -_-) I should check for the surrounding cells, If they make up to
        be 1, I'll add 1 and update the current cell.

        What does that do? That's it, Question is over.
        You have your grid size in your goal cell, store it in max_side and square it, Do whatever you want

        But wait, What if a surrounding is 0, link will break right?
        Right, That's why update the current cell by adding 1 to the 'min value of surrounding cells'.

        Okay that's good, But what if the square of 1's is bigger?
        That's the magic of DP, You already checked for one square, You updated the goal cells, Now when you face more ones, You'll update more goal cells, grid size goes form 1 to 2 and whne finally dp reaches the final 2*2 of the big square, a Min of 2 will be incremented, which equal 3. So bigger problems will be tackled by DP, By using the past results

        Now you tell me, Why will you need a DP grid of an extra row and col?
        To check the first element extreme lefts and tops , Also the start cell of the grid

        That's it, Was this so difficult? Have you not done the same question atleast 10 times now?
        That's it, Cool

    '''
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix or len(matrix) < 1:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1] , dp[i-1][j] , dp[i][j-1]) + 1
                    max_side = max(max_side , dp[i][j])
        
        return max_side * max_side # Area of square