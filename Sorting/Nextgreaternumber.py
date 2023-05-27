class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))

        # Logic: String Sorting

        '''
            In this problem, We need to make the smallest possible greater integer than the given number
            Now something I have learned from here, and something you should too is that, When you swap the first smaller element from the last i.e. nums(i-1) < nums(i) with the first greater element nums[j] > nums[i-1], You get the next possible smallest greater number

            After finding these elements, swap them with each other, and you get the permutation of the smallest greater number

            Now if you reverse this number i.e. reversal from nums[i:][::-1], You get the smallest possible greater permutation

            To check if it is a 32 bit no. or not, if n < 2**31 is the way to go

            That's it :coinflipper: ;)

        '''

        for i in range(len(nums)-1,-1,-1):
            if nums[i-1]<nums[i]:
                break

        if i == 0:
            return -1

        for j in range(len(nums)-1,i-2,-1):
            if nums[j]>nums[i-1]:
                break

        nums[i-1],nums[j] = nums[j],nums[i-1]

        nums[i:] = nums[i:][::-1]
        res = int(''.join(nums))

        return res if res < 2**31 else -1