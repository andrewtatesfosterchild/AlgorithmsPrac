class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Logic: Hashmap as counter

        '''
            Fairly simple approach, The only thing worth remembering here is the logic with which we find the element in hashmap with value 1

        for key , value in hashmap.items():
            if value == 1:
                return key
        
        could've even used,
            for key in hashmap:
                if hashmap[key] == 1:
                    return key
        '''

        hashmap = {}


        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            
            else:
                hashmap[nums[i]]+=1
        
        for key , value in hashmap.items():
            if value == 1:
                return key

        # Logic: A more concise bitwise approach

        '''
            Mind you I need to work on this solution myself

            This is a very powerful solution to find single elments in an array , Remember it

            The algorithm takes advantage of the XOR operation properties, where XOR-ing a number with itself cancels out the bits, and XOR-ing with 0 leaves the bits unchanged.

            Update the "ones" variable:

            Perform the XOR operation between "ones" and the current number: ones = ones ^ num.
            Perform the AND operation between the result and the complement of "twos": ones = (ones ^ num) & ~twos.
            This step ensures that any bit that appears twice in "twos" is not considered as a single occurrence in "ones."

            Update the "twos" variable:

            Perform the XOR operation between "twos" and the current number: twos = twos ^ num.
            Perform the AND operation between the result and the complement of "ones": twos = (twos ^ num) & ~ones.
            This step ensures that any bit that appears twice in "ones" is not considered as a double occurrence in "twos."



            That's it, :coinflipper: ;)
        '''

        ones = 0 # One occurences so far
        twos = 0 # Two occurences so far

        for num in nums:
            ones = (ones ^ num) &~twos 
            twos = (twos ^ num) &~ones
        

        return ones
