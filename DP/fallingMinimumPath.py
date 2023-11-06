class Solution:
    # Logic: classic DP sum

    '''
        Instead of targeting what is visible, Sometimes you have to target things which try to hide in the background. Because those are the ones that are really important

        Here , Instead of finding a way to target middle element by doing j // 2 and what not , You can simply carget j == 0 and j == -1 separately , and what remains is the middle , Which can be targeted separately

        For the edge elements you have two paths adding into them , take the min of the upper element and upper lower left element or lower right element depending on j == 0 or j == len(matrix[0])

        For the middle elements , Three paths will add into them , Take the minimum of matrix[i-1][j-1] , matrix[i-1][j] and matrix [i-1][j+1]

        Finally , Run a for loop to find the minimum path sum on the last row of the matrix

        That's it , Tell me was this something so difficult? Have we not done this before?
        That's it , Cool
    '''
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    continue

                elif j == 0:
                    matrix[i][j] += min(matrix[i-1][j] , matrix[i-1][j+1])
                
                elif j == len(matrix[0]) - 1:
                    matrix[i][j] += min(matrix[i-1][j] , matrix[i-1][j-1])
                
                else:
                    matrix[i][j] += min(matrix[i-1][j] , matrix[i-1][j-1] , matrix[i-1][j+1])
        
        return min(matrix[-1][x] for x in range(len(matrix[0])))