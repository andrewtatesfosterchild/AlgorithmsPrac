class Solution:
    def checker(self,row):
        temp = [x for x in row if x!='.']
        return len(temp) == len(set(temp))

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Logic: 3 checks, Rows, Columns and Subgrids

        '''
            Each row must contain the digits 1-9 without repetition.
            Each column must contain the digits 1-9 without repetition.
            Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

            These three conditions make a sudoku valid, And these three conditions make our solution limited to three checks only, Check the rows if any number is repeated, Check the columns if any number is repeated, and finally check the subgrid if any number is repeated

            What can you make of this? This is a mere traversal problem with some checking involved, That's it, 50% done.

            Let's look at the checking logic first,
                    def checker(self,row):
                        temp = [x for x in row if x!='.']
                        return len(temp) == len(set(temp))
                    
                    It generates a temp list by removing empty cells represented by '.'
                    Then, If the length of this list is equal to the length of the set of that list,
                    It simply means that all the elements are unique and good to go, Else it returns false
            
            Now let's proceed to checking the rows,
                for row in board:
                    if not self.checker(row):
                    return False
                
                Very basic stuff, Just plainly checking the rows
            
            Checking the columns now, * Remember this column traversing logic, It's extremely good
                for col in range(9):
                    column = [board[i][col] for i in range(9)]
                    if not self.checker(column):
                        return False
                
                It iterates with an index col from 0 to 8,
                And generates a list column which contains all the coumn elements from each row

                Then send this to checker, And get the result
            
            Finally, We check the 3x3 subgrids,

                For the subgrids, We start by targeting the top-left element of each subgrid i.e. (i,j)

                for i in range(0 , 9 , 3):
                    for j in range(0, 9 , 3): 
                
                Imagine , It generates (i,j) == (0,0) , (0,3) , (0,6), (3,0) , (3,3) , (3,6) , (6,0) , (6,3), (6,6)

                Now we got the top-left elements of all subgrids, But we need the subgrid elements, For that we need to add the offset

               Therefore, To complete the for loops,
                    for i in range(0 , 9 , 3):
                        for j in range(0, 9 , 3): 
                            subgrid = [board[x][y] for x in range (i,i+3) for y in range(j, j+3)]

                            Here, The subgrid is a list generated by the offsets (i,i+3) and (j, j+3), Thus covering all the elements of the subgrid

                        Finally we pass this list to the checker function and get the result

                If everything works, We return True

                That's it, :coinflipper: ;)
                    
        '''

        # Checking rows
        for row in board:
            if not self.checker(row):
                return False
        
        # Checking columns
        for col in range(9):
            column = [board[i][col] for i in range(9)]
            if not self.checker(column):
                return False
        
        # Checking 3x3 Subgrids
        for i in range(0 , 9 , 3): # These two loops combined, target top-left element of each subgrid i.e. (i,j)
            for j in range(0, 9 , 3): 
                subgrid = [board[x][y] for x in range (i,i+3) for y in range(j, j+3)] # i, i+3 and j, j+3 is the offset which contains all the subgrid elements , Generates subgrid in the form of a list
                if not self.checker(subgrid):
                    return False


        
        return True