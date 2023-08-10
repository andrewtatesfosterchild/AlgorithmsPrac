class Solution:

    # Logic: Sliding Window + Queue!

    '''
        Wouldn't call this a brilliant question, But definitely a brilliant intuition.

        Why if, A window slides, Can't we take the max of the window and just append it? Done right?
        Well, That's technically not incorrect, You're absolutely right

        But this will cause problem when the window size is large, Should you fathom 50000 elements and counting the max out of it will be horsejob

        So we can take the max(window) approach as bruteforced. But what if we use a data structure which is perfect to find the maximum among k elements? That's right, A Deque.

        One very important intuition, Which speaks out "Use a Queue":
        Observe carefully , As you slide a window, You encounter new elements.
        But, As soon as you encounter an element that is larger than all the previous elements, Those elements will NEVER be used again. Why? Imagine this, Take [1 , 2 , 3 , 4 , 1] for example,
        Imagine the window expanding first uptil 3 elements, 1... 2... 3. Now slide the window, Will you ever use 2 again when 3 is present already and is larger than 2? You get my point now.

        You can't do the same with next elements, They all should be accounted for since they might contain a larger element than 3 itself.

        So what are we doing here? We are keeping the maximum and scraping all the obsolete elements, One's that don't need to be accounted for anymore. That's the intuition behind using Queue for this problem. Keeping the maximum till it's valid and scraping the obsoletes

        We are storing indexes in queue to compare if an element in queue falls outside the range of current window, If it does we popleft

        First lets expand the window,
        While expanding we append every index to queue, All indexes get a chance
        However the while loop starts comparing the current nums[i] with the dq's last stored index and it if falls smaller, dq.pop()
        Ofcourse new ones will be appended, But they might get popped later too

        When we start sliding the window, Everything else remains the same actually , We just need to account for the case that the current maximum in deque belongs to the previous window, Then we must pop it. Then the while loop and append conditions further set up the maximum same as they did in expanding phase. When the window is mature, Start appending nums[dq[0]] # The maximum element from every window to the res

        That's it, Cool , Easy


    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l , window = 0 , []
        dq = deque()

        for i in range(len(nums)):

            # Expand the window
            if i - l + 1 < k:
                while dq and nums[i] >= nums[dq[-1]]: # Only the meximum survives
                    dq.pop()
                dq.append(i)
            
            # Slide the window
            else:
                if dq and dq[0] == i - k: # Element fell outside window , This is precisely why we inserted indexes in dq instead of elements themselves
                    dq.popleft()
                while dq and nums[i] >= nums[dq[-1]]: # Only the maximum survives
                    dq.pop()
            
                dq.append(i)
                window.append(nums[dq[0]]) # Append the maximum
                l+=1 # Slide the window
            
        
        return window # Return answer