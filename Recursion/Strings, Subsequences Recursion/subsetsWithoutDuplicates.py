class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #Logic: Subsets problem with recursion

        '''

            What's the logic behind for loop in helper...

            If the previous element is already considered , Do not consider it again as it will cause a duplicate subset, Thus all the combinations will be covered by the time the loop has finished
            Why was sorting needed? The recursion totally relies on the prev element for determining if it is a duplicate or not, So sorting ensures duplicate elements stay together!

            Everything else is the same, The recursion the logic, Same as subset without duplicate , take not take method. That's it

        '''

        return self.helper([] , sorted(nums) , 0)
    
    def helper(self , p , up , prev):
        
        res = [p]

        for i in range(prev , len(up)):
            if i > prev and up[i] == up[i-1]: # Checking for duplicate
                continue
            else:
                res.extend(self.helper(p + [up[i]] , up , i + 1)) # Merging case
        
        return res
                

        