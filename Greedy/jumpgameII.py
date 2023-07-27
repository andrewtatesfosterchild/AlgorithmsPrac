class Solution:
    # Logic: Greedy approach
    '''
        At every jump , We greedily choose to maximize our reach in order to minimize our jumps
        We run a loop till len(nums) - 1 to check our reaches , Since at n you've already reached
        Initially, jumps , maxReach and curReach are all 0

        Inside the loop,
        MaxReach keeps a track of maximum index reached so far

        imagine now, until we reach maxReach , We are in air , We took a big leap of faith, and until we reach the maxReach's index, The jump continues. This is the essence of the next line

       i == curReach, You have finally landed on the maxReach index, Its time to update the curreach to the current maxReach

        curReach = maxReach

        Now if curReach is beyond len(nums) - 1
        Instantly return the number of jumps as it has surpassed the array

        Now if i is beyond maxReach , No plausible solution exists
        return 0

        At the end,
        return jumps

        That's it


    '''
    def jump(self, nums: List[int]) -> int:
        jumps , curReach , maxReach = 0 , 0 , 0
        for i in range(len(nums) - 1):
            maxReach = max(maxReach , i + nums[i])
            if i == curReach:
                jumps += 1
                curReach = maxReach
            if curReach >= len(nums) - 1:
                return jumps
            if i >= maxReach:
                return 0
        return jumps
        