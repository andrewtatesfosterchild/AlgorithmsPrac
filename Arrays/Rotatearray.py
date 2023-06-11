class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k = k%len(nums)

        # Logic: 3 reverses and done

        '''
            To rotate an array is to reverse it 3 times,

            Firstly partition it so as the given rotation no. (k) is the number of elements from the end of array
            (These elements will be pushed forward in indices)

            Then, Reverse these partitions individually, Then reverse the array as a whole

            Also, Notice we k%len(nums) initially, Why?
                Because if k is a bigger val than len(s) then everytime k = len(s) while performing rotations, We will get the original array, Now this can cost us so much time and hence let's just avoid this and make our job efficient

            That's it, :coinflipper: ;)


        '''

        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(arr, start , end):
            li = start # left index
            ri = end # Right index

            while (li < ri): # This reversing logic is too good, Remember it
                temp = arr[li]
                arr[li] = arr[ri]
                arr[ri] = temp

                li+=1
                ri-=1
        
        reverse(nums, 0 , len(nums) - k - 1) # Left part
        reverse(nums, len(nums) - k , len(nums) - 1) # Right part
        reverse(nums, 0 , len(nums) - 1)  # Total array

        

        