class Solution:
    # Logic: Interval scheduling problem , Greedy approach

    '''
        Everytime I should try to minimize my value of k, So as to get minimum number of overlaps

        For this purpose, We sort the given array based on the end times, and set a k value

        k is the end time of the current interval, If this k is smaller than the start time of the next interval, No overlap occurs and we update the k to the endtime of this current interval

        now, on the other hand, if x is smaller than k , Then an overlap occurs and this interval has to be removed
        thus, ans+=1

        return ans

        That's it, That's the interval scheduling problem
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:x[1]) # This line sorts the array according to the end intervals y, **This is an important sorting technique, Remember it

        k = intervals[0][1] # Setting the initial valur of k as end of first interval

        ans = 0

        # After sorting, Start iterating over intervals
        # I check in each interval after first one, If start is greater than or equal to k, If that's the case then no overlap occurs and the new k value is the end of this inverval

        # However, If x < k, It means there is an overlap and this interval must be removed

        for x , y in intervals[1:]: # x & y denote start & end of each interval, **This is an important looping technique, Remember it
            if x >= k: # start of this interval is less than end of prev interval
                k = y # set k = the end of this interval
            else: # x is smaller, meaning an overlap, Thus discard it
                ans+=1
        
        return ans