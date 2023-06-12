class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Logic: Very core concept of 2D arrays, Transposition + Reflect = Rotation by 90 deg (clockwise)

        '''
            This is an imp problem

            Here we learn, How to transpose and reflect in 2D arrays

            reflection is easy, It's straight up reversal of rows

            But transposition is a bit logical,
                Transposition essentially means turning rows into columns and columns into rows

                Now, It's fairly easy to do this, If the intuition clicks correctly in this equation:

                for i in range(len(matrix)):
                    for j in range(i+1 , len(matrix)):
                        matrix[i][j] , matrix[j][i] = matrix [j][i] , matrix [i][j]
                    
                    * Why do we start the second loop from i+1?
                        It just swaps the i+1th element of j with jth element of i+1, And that's basically it!
                        That's transpose
                        Try it out with a pen and paper and you'll get it surely
                
                After that, There's nothing more in this question, It's done

                :coinflipper: ;)
        '''



        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i+1 , len(matrix)):
                    matrix[i][j] , matrix[j][i] = matrix [j][i] , matrix [i][j]
        
                
        def reflect(matrix):
            for row in matrix:
                li = 0
                ri = len(matrix) - 1
                while li < ri:
                    temp = row[li]
                    row[li] = row[ri]
                    row[ri] = temp

                    li+=1
                    ri-=1

        transpose(matrix)
        reflect(matrix)