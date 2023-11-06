class Solution:

    # Logic: Defying the bounds of normal recursive permutation

    '''
        This is similar to the next greater number problem in some sort
        In next greater number we modified the suffix to get the minimal increase in the number , In a similar sort of fashion we solve the next permutation problem

        At first look this might look like another take not take problem.
        However, Observe closely, When it is mentioned In-place return,
        Take not take becomes difficult, We need to go with primary instintual mathematic approach

        Next permutation,
        Problem is fairly simple. We have to find the next permutation and we cannot use recursion, So what do we do? Some suffix play, yes.

        First , understand that we are supposed to find the next permuation in the increasing lexographical order.

        For finding the next greater of anything , We increase the right side, The units place for instance, See? Primary instinctual math

        Here, For the order, We will find the longest decreasing subarray
        from the end

        Now what if the longest decreasing subarray is the whole array itself, Then? Then just reverse the nums, Because you my friend just encountered the case of 'The last greatest possible permutation' , Solution? Go to the first permutation since it is the next in lexographical order

        Wait but I did not encounter that case!
        Okay then, Let's find the pivot, Pivot is the element left adjacent to the element from which decreasing subarray begins

        Once you have the pivot , We need to swap this pivot with the first greater number you find from the end of the decreasing subarray

        Okay done, Now what Sherlock -_-

        Just reverse the decreasing subarray

        That's it , Primary instincts and 6th grader math
        Was this so difficult? Okay , Cool
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        r , j = len(nums) - 1 , len(nums) - 1

        while r > 0 and nums[r-1]>=nums[r]:
            r-=1

        if not r:
            nums.reverse()
            return
        
        # pivot = nums[r-1] # Reference problem*

        for i in range(j , r-1 , -1):
                if nums[r-1] < nums[i]:
                    nums[r-1] , nums[i] = nums[i] , nums[r-1]
                    break

        while r < j:

            temp = nums[r]
            nums[r] = nums[j]
            nums[j] = temp

            r+=1
            j-=1