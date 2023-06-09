class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        i, j = 0, len(a) - 1

        # Logic: Greedy two pointer approach

        '''
            We work in 4 parts here:

            First we find a_suffix and b_prefix

            Then we find b_suffix and a_prefix

            If any of these are palindromes we return true, else false

            That's it :/ , :coinflipper: ;)
        '''

        while i < j and a[i] == b[j]: # Keep inc i and dec j till a[i] == b[j]
            i+=1
            j-=1
        s1,s2 = a[i:j+1] , b[i:j+1] # Assign potential palindromic substring values to s1 and s2


        i,j = 0 , len(a) - 1 # Reset pointers

        while i < j and b[i] == a[j]: # Keep inc i and dec j till b[i] == a[j]
            i+=1
            j-=1
        s3,s4 = a[i:j+1], b[i:j+1] # Assign potential palindromic substring values to s3 and s4


        return any(s == s[::-1] for s in (s1,s2,s3,s4)) # Generator function to check if any substring == rev(substring) if yes return true else false