class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Logic: Sliding window again with a kick

        '''
            This was fairly easy this time

            We start with 3 variables as usual
            start , windowsize, total = 0 , float('inf') , 0

            The goal is to minimize windowsize and achieve the target as total

            So let's start

            for i in range(len(nums)):
            i is my right bound, my upper bound pointer
            
                total += nums[i]
                I keep adding the right bound to the total

                while total >= target:
                Until my total exceeds the target, Only then I'll meet a potential subarray

                windowsize = min(windowsize, i - start + 1)
                total -= nums[start]
                start+=1

                I keep minimizing the windowsize with every while loop iteration, with the current size of window. Till my total >= target I keep shrinking my window from the left by incrementing the start variable. This happens till the total becomes less than target.

                Due to the >= condition, There might come a hit where the windowsize is minimized to the current subarray and then we check for further optimized results by moving the upper bound i in the next iteration and repeating the same process

            That's it, :coinflip: ;)

        '''
        
        start , windowsize, total = 0 , float('inf') , 0

        for i in range(len(nums)):

            total += nums[i]

            while total >= target:
                windowsize = min(windowsize, i - start + 1)
                total -= nums[start]
                start+=1
        
        return windowsize if windowsize != float('inf') else 0

            

