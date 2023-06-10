class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Logic: ez qtn, sorting + lin search

        '''
            Nothing to this question really, You convert to a set & you sort the set, 
            Now duplicates are gonea and nums is ordered

            start with two vars, currstreak, longstreak = 0 , 0

            Now loop through the entire array and keep incrementing currstreak as we encounter sequences i.e.
                    if nums[i] - nums[i-1] == 1:
                    currstreak+=1

                    else:
                    currstreak = 0

                    * Now keep it in mind, When a streak ends, The last element is unaccountd for, We'll use this fact later

            At the end of each iteration,

                    longstreak = max(longstreak, currstreak)
            
            return longstreak + 1
             * Why +1?, Because the last element in currstreak was not counted in the streak, As mentioned in above fact

             That's it, :coinflipper: ;)
            
            
        '''

        if len(nums) == 0:
            return 0
        
        else:

            nums = sorted(set(nums))

            currstreak, longstreak = 0 , 0

            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] == 1:
                    currstreak+=1
                
                else:
                    currstreak = 0
                
                longstreak = max(longstreak, currstreak)
        
        return longstreak + 1 # +1 to account for the current element which was ignored by currstreak
        
            