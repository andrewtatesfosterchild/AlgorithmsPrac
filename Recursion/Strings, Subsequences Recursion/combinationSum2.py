class Solution:
    # Logic: Subset problem ; Recursive subsets

    '''
        Combination sums 2 huh
        What's different? This time, Each number of candidates can be used only ONCE i.e. each instance can be used once
        Each combination must be unique

        The first intuition which comes to mind is that we need to change the start index everytime , So that previous instances of a number are not counted for twice

        So we will do that further in the algorithm

        First we sort, Because we need to filter out for duplicates in the latter parts

        We enter the recursive function:

            First check if target == 0: return [p] , we return the current combination

            if not,

            we set a localized answer ans = []

            Here comes the magic:
            for i , num in enumerate(up): starts a loop for making recursive calls
                
                if i > 0 and up[i] == u[i-1] # This means that it is a duplicte case and the previous number is already accounted for in some or the other combination, So we cant account for it again

                *And how do we know that prev number is accounted for?
                That's precisely why i > 0 condition is used here, well besides avoiding list index out of range but, suppose in this example [10,1,2,7,6,1,5]:

                Sorted array: [1 , 1 , 2 , 5 ,  6, 7 , 10]
                when loop begins, i > 0 condition fails, we dont check for prev num.
                target condition fails , loop stays intact
                we send a recursive call of i + 1 and thus 1 gets used in a combination, That's why we are using each element atleast once in a combination
            
                Coming out of example, Then and only then we send recursive call adding the current element to processed, Subtracting current element from target and checking if target == 0 in the next recursion call.

                ans.extend(self.helper(p + [num] , up[i + 1:] , target - num)) # Here, i + 1 is what we talked about earlier, Moving the start index for every recursive call

            That's it, Was this something new? Was this something we haven't solved atleast 10 times? :/


    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)

        return self.helper([] , candidates , target)
    
    def helper(self , p , up , target):

        if target == 0:
            return [p]
        
        ans = []
        
        for i , num in enumerate(up):
            # step 1: Excluding same elements
            if i > 0 and  up[i] == up[i-1]:
                continue
            
            #step 2: determining the stop condition for the loop
            if target - num < 0:
                break
            
            #step 3: recursively calling helper funtion for every num
            ans.extend(self.helper(p + [num] , up[i+1:] , target - num))

        return ans