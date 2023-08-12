class Solution:
    # Logic: Naive Bruteforced ; recursion
    # def longestPalindromeSubseq(self, s: str) -> int:

    #     seq = self.helper("" , s)
    #     maxval = 0
    #     count = 0

    #     for sequence in seq:
    #         maxval = max(maxval , count)
    #         count = 0
    #         i = 0
    #         j = len(sequence) - 1
    #         while i <= j and sequence and sequence[i] == sequence[j]:
    #             count+=2
    #             i+=1
    #             j-=1
    #         if len(sequence) % 2 > 0:
    #             count-=1
        
    #     return maxval


    # def helper(self , p , up):

    #     if up == "":
    #         return [p]
        
    #     ans = []

    #     ans.extend(self.helper(p + up[0] , up[1:]))
    #     ans.extend(self.helper(p , up[1:]))

    #     return ans

    # Logic: Memoized recursion

    '''
        What's the primary instinct while solving this problem?
        Search for all subsequences and then filter them out later, Good, But it will cause TLE / MLE

        To make it more efficient, We need to memoize recursion

        What's the unique parameter? Tha'ts right, The tuple of (l , r)
        Why? Think logically, The string is the same, So same l , r will always mean the same part of the string

        What remains is what to return when,
        Now see when l > r, Definitely string does not exist and we return 0

        when l == r , String exists and has 1 char, we return ans + 1 since well one char means a palindrome

        when s[l] == s[r], We hit a palindromic case, ans = self.helper(s , l + 1 , r - 1) + 2
        Why 2 , 2 characters are matching, start and end

        else:
            we seek inside the substrings of the current subsequence
            ans = max(self.helper(s , l , r - 1) , self.helper(s , l + 1 , r))

        Memoize the answer
        self.visited[(l , r)] = ans

        return ans

        That's it , Easy , Cool
    '''
    def longestPalindromeSubseq(self, s: str) -> int:
        self.visited = {}
        return self.helper(s , 0 , len(s) - 1)
    
    def helper(self , s , l , r):
        if (l , r) in self.visited:
            return self.visited[(l , r)]
        
        ans = 0
        
        if l > r:
            return 0
        
        if l == r:
            return ans + 1
        
        if s[l] == s[r]:
            ans = self.helper(s , l + 1 , r - 1) + 2
        else:
            ans = max(self.helper(s , l + 1 , r) , self.helper(s , l , r - 1))
        
        self.visited[(l , r)] = ans

        return ans