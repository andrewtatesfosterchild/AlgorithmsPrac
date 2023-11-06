class Solution:
    # Logic: Classic DP sum ; Two ways to go from each element

    '''
        What was the intuition?
        What was the only inutition this sum needed?

        We start from the bottom and try to minimize the apex
        For each element that is above the base level of the triangle there are two ways to reach, One from the lower left of that element, Other from the lower right of that element, We just have to select the min of those two paths

        The base level remains unchanged since we need to travel upwards
        That's it, Finished, What was so difficult? Hawwa banaake rakha hai bas, Cool
        Done
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 1 , -1 , -1):
            for j in range(i+1):
                if i == len(triangle) - 1:
                    continue
                else:
                    triangle[i][j] += min(triangle[i+1][j] , triangle[i+1][j+1])
        
        return triangle[0][0]