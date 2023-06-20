class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        # Logic: Sliding window algorithm

        '''
            This is nothing but sum of elements in a window, If you imagine it correctly

            The window size is given by 2 * k + 1, where k = offset, twice k gives left and right halves of window and + 1 gives the central element, together 2 * k + 1 gives complete array

            First, initialize averages = [-1]*len(nums)

            Now to handle some edge cases, k == 0, return nums, straightforward

            if 2 * k + 1 > n, This means the size of window is greater than len of given array, Thus return averages as no element can produce an average in this case

            Now starts the sliding window,
                window_sum = sum(nums[:2 * k + 1]) gives the sum of the first window
                Imagine the centre of this window, it will be 'k', Think about it ;)
                So, averages[k] = window_sum // (2 * k + 1) i.e sum // window size


            Now start rolling this window,
                for i in range(2 * k + 1, len(nums)):
                    # nums[i - (2 * k + 1)] = prev element
                    # nums[i] = curr element
                    window_sum = window_sum - nums[i - (2 * k + 1)] + nums[i]
                    averages[i - k] = window_sum // (2 * k + 1) * why i - k?
                    remember the first valid index as k? i - k is the offset, It gives the next valid centre if you think about it, subtracting k from the curr value of i, Thus, averages[i-k]

            return averages

            That's it, :coinflipper: ;)


        '''

        if k == 0:
            return nums
        
        n = len(nums)
        averages = [-1]*len(nums)

        if 2 * k + 1 > n:
            return averages
        
        else:
            window_sum = sum(nums[:2 * k + 1])
            averages[k] = window_sum // (2 * k + 1)

            
            for i in range(2 * k + 1, n):
                window_sum = window_sum - nums[i - (2 * k + 1)] + nums[i]
                averages[i-k] = window_sum//(2 * k + 1)
        
        return averages