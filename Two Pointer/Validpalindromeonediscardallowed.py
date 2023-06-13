class Solution:
    def validPalindrome(self, s: str) -> bool:

        # Logic: Simple question if you don't get stuck at 'This'

        '''
            Which element to skip?
            Skip the left, Skip the right, Skip both

            All of these choices won't work, Testcases WILL fail

            No shit sherlock, So what's the way out?
            Pretty easy, make two strings from source string, one discards left element
            The other discards the right element

            If either of them matches their reverse, Return True else False

            That's it, Over ¯\_(ツ)_/¯ 

            :coinflipper: ;)
        '''
        
        if len(s) == 1: # 1 letter always palindromic
            return True

        i , j = 0 , len(s) - 1 # Setting two pointers

        while i <= j and s[i] == s[j]: # Matching first and last elements & Decrementing counters
            i+=1
            j-=1

        if i > j: # All elements got traversed without mismatch, Thus return True
            return True
        
        else: # There was a mismatch, Try to remove the mismatching elements and check if any of these strings become palindromic

            str1 = s[0:i] + s[i+1:] # Discarding left element
            str2 = s[0:j] + s[j+1:] # Discarding right element

            if str1 == str1[::-1] or str2 == str2[::-1]:
                return True