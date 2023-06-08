class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        # Logic: bs question quite literally
        '''
            Binary searching in 2D arrays, Duh -_-
        '''

        def binarysearch(arr):
            s = 0
            e = len(arr) - 1

            while (s<=e):
                
                mid = s + (e-s)//2

                if arr[mid] < 0:
                    e = mid - 1
                else:
                    s = mid + 1

            return len(arr[s:])
            

        for i in range(len(grid)):
            count+= binarysearch(grid[i])
        
        return count
