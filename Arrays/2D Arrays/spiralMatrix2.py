class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # Logic: Layerwise matrix traversal

        '''
            The core concept of such problems is to traverse the matrix in layers
            and to determine the underlying pattern

            The main thing you should focus on is the pattern next,
            For this question, We are supposed to integers in spiral order inside a matrix till n**2 is not achieved

            After this, let's proceed to traversing

            for layer in range ((n + 1) // 2): * Why ((n + 1) // 2)? Because ((n + 1) // 2) gives the number of layers always, Try it!

                # Right Direction

                for i in range(layer , n - layer): (layer -> row no. (depicts the top left element of current layer) , n - layer -> Right edge of current layer)
                res[layer][i] = count # Notice how row remains constant in right traversal
                count+=1

                # Downward Direction

                for i in range(layer + 1 , n - layer): (layer + 1 -> Skipping the top right element which was already set in previous right transversal , n - layer -> Bottom edge of the current layer)
                    res[i][n - layer - 1] = count # Notice how the column remains constant as the right wall of current layer here
                    count+=1
                
                # Left Direction

                for i in range(layer + 1 , n - layer): (layer + 1 -> Skipping the rightmost element which was already set by previous downward traversal , n - layer -> Left edge of the current layer)
                    res[n - layer - 1][n - i - 1] = count # Notice how the row remains constant as the bottom wall of current layer here whilst [n - i - 1] depicts subtracting 1 from the above range till leftmost column is hit
                    count+=1
                
                # Upward Direction

                for i in range(layer + 1 , n - layer - 1): (layer + 1 -> Avoiding the bottomleft element which was previously modified in left traversal, n - layer - 1 -> Hitting the top wall and leaving the topmost element out)
                    res[n - i - 1][layer] = count # Notice how the column stays constant as the left wall of current layer whilst [n - i - 1] depicts traversing reverse by subtracting 1 till you hit the top wall of current layer
                    count+=1

        return res after this

        That's it, :coinflipper: ;)

        '''
        res = [[0 for _ in range(n)] for _ in range(n)]
        count = 1

        for layer in range ((n + 1) // 2):

            # Right Direction

            for i in range(layer , n - layer):
                res[layer][i] = count
                count+=1

            # Downward Direction

            for i in range(layer + 1 , n - layer):
                res[i][n - layer - 1] = count
                count+=1
            
            # Left Direction

            for i in range(layer + 1 , n - layer):
                res[n - layer - 1][n - i - 1] = count
                count+=1
            
            # Upward Direction

            for i in range(layer + 1 , n - layer - 1):
                res[n - i - 1][layer] = count
                count+=1
        
        return res
        
