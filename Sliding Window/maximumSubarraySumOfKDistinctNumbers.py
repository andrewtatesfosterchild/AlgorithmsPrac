class Solution:

    # Logic:  Sliding window with hashmap

    '''
        Not to shabby kid , I'm proud of you , Solved a sliding window by yourself. Keep up the good work.
        
        What was the intuition behind this problem?
        If I can somehow get the number of distinct numbers in my hashmap , I can makea condition out of it.
        That's where count variable came into the picture

        Everytime I encountered an element which is not in the hashmap, It is a unique one , Let's increase the count

        If the window is less than k, Let's increase the size by going into the next iteration

        Now however, If the window is of k size, Now we need to check if the count is equal to k , i.e. the elements we have are all different , If yes, Good this is a valid window , Let's try to see if this is the max so far, But here came an issue , TLE , Why? Because we were finding sum(nums[l:r+1]) in this line. This is where the sum variable walks in. Each time you encounter a distinct element add it to the sum in the for loop itself, And if the conditions meet just try to maximize windowsum with that sum. Same thing.

        If the window does not have k distinct elements, No problem just reduce the nums[l] from hashmap and even pop it if it becomes 0. But when the popping case comes , The count will reduce by one and the sum will reduce by a nums[l], As you're removing an element from the hashmap

        That's it , Cool

    '''
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        l , windowsum , count , sum = 0 , 0 , 0 , 0
        hashmap = {}

        for i in range(len(nums)):

            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
                count+=1
                sum += nums[i] # TLE Fix
            hashmap[nums[i]]+=1

            if i - l + 1 < k:
                i+=1
            else:
                if count == k:
                    windowsum = max(windowsum , sum)
                hashmap[nums[l]]-=1
                if hashmap[nums[l]] == 0:
                    hashmap.pop(nums[l])
                    sum-=nums[l]
                    count-=1
                l+=1

        return windowsum