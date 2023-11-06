class Solution:

    # Logic: Classic DP 2D array sum

    '''
        Remember this, DP solves the problem by solving the smallest problem first, Then smaller, Then small , Than large ones

        First , We setup up a 2D DP array of n * n where n is the length of input string and dp[i][j] represents whether a string is palindromic or not
        
        initially all the values are set to False
        ans = [0 , 0] will represent the bounds of the string

        Now,

        This solution can be broken down into 3 parts:

            Part 1: Solving for strings of length 1
                for i in range(n):
                    dp[i][i] = True
                Pretty logical , Every string of length 1 is a palindrome
            
            Part 2: Solving for strings of length 2
                for i in range(n - 1):
                    if s[i] == s[i+1]:
                        dp[i][i+1] = True
                        ans = [i , i + 1]
                    Pretty logical again, Comparing two characters as equal , We can state a palindrome or not
                Setting the answer on the fly as we will always get a palindrome greater than the old one
            
            Part 3: Solving for lengths 3 and above
                for diff in range(2 , n): Marking all differences in bounds of 2 and more, i.e. strings of length 3 or more
                    for i in range(n - diff): # Marking i as the starting index
                        j = i + diff # Marking j as the ending index

                        if s[i] == s[j] and dp[i+1][j-1]:
                        This is the magical moment where we use the past results of DP, Remember we calculated for smaller strings before? Now we are using it

                            dp[i][j] = True
                            Now the great part is THIS result will be used by some string of greater length!
                            ans = [i , j] on the fly, again.
            
            i , j = ans

            return s[i:j+1]

            That's it, Hawwa banaake rakha hai bas
                


    '''
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = [0 , 0]

        for i in range(n): # All single chars are palindromes
            dp[i][i] = True
        
        for i in range(n - 1): # Checking for substrings of length 2
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i , i+1]
        
        for diff in range(2 , n): # Difference of indices = 2 , meaning from substrings of length 3
            for i in range(n - diff): # Perfectly sets the start and end indexes
                j = i + diff # Setting the end index

                if s[i] == s[j] and dp[i+1][j-1]: # If end characters are equal and dp states the insides are equal too
                    dp[i][j] = True
                    ans = [i,j]
        
        i , j = ans
        return s[i:j+1]