class Solution:
    # Logic: Hashmap

    '''
        Hashmap will store all the indices which contain zeroes

        Later, Use these indices and turn the rows and columns into 0

        That's it , Easy , Cool
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        hashmap = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    hashmap[(i , j)] = 1

        for keys in hashmap:
            i , j = keys

            x = 0
            while x < n:
                matrix[i][x] = 0
                x+=1
            
            x = 0
            while x < m:
                matrix[x][j] = 0
                x+=1