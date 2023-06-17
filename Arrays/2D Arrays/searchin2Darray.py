class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Logic: Good old bs

        '''
            Ain't explaining this bs -_-
        '''

        def binarysearch(row , target):

            s = 0
            e = len(row) - 1

            while s <= e:
                mid = s + (e-s)//2

                if target == row[mid]:
                    return True

                elif target > row[mid]:
                    s = mid + 1

                else:
                    e = mid - 1
            
            return False
        
        for row in matrix:
            if binarysearch(row,target):
                return True
        
        return False