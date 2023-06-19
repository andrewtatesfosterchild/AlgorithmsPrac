class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx , maxval , target = 0, 0, len(nums) - 1

        # Logic: Greedy approach

        '''
            In this solution, We check at each step whether including the current case will take us to the favourable outcome or not, i.e. 'A Greedy algorithm'

            Firstly, We initialize index, maxval and target respectively:
                idx , maxval , target = 0, 0, len(nums) - 1
            
            The approach we shall follow is simple, At every index, Check the maximum value that a jump can reach. If that max jump is >= target, Then sure it's possible to reach target
            If not, and the loop ends, Target can never be reached and we return False

            Let's start with the while loop
                while (idx<len(nums)):

                    maxval = max(max, idx + nums[idx]) where idx + nums[idx] denotes the maximum jump that can be made from current index

                so, maxval keeps a track of maximum jump that has been made so far

                Now things are pretty simple,
                    
                    if (maxval>=target):
                        return True
                    
                    elif (maxval <= target and nums[idx] <= 0) i.e. A zero is encountered before reaching maxval, No jumps can be made now
                        return False
                    
                    idx+=1
            
            Thus, It will calc maxval on each index to see if it can reach target, And if the loop ends without encountering anything and index itself reaches maxval

            return False

            That's it, :coinflipper: ;)

            
        '''

        while (idx<len(nums)): # < len(nums) because it includes all elements, Thus including all edge cases

            maxval = max(maxval, idx + nums[idx]) # update max jump so far

            if maxval >= target: # target reached
                return True
            
            elif (maxval <= target and nums[idx] == 0): # Target unreachable
                return False
            
            idx+=1 # increment to next number
        
        return False # No case hit