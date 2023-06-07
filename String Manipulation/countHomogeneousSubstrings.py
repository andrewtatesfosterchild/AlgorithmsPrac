class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 1 # Initially the current char will be the only homogeneous substring char, Thus count = 1
        res = 0

        # Logic: very similar to substrings with only 1's

        '''
            This question is very similar to substrings with only 1's
            A major diff is that, That prob had only 1's and 0's and thus split(0) was viable but here,
            It's not
            Therefore we use count approach

            We keep a count of all homogeneous characters spotted
            When a homogeneous substring ends, We add count*(count - 1)//2 to the result ( if count>1 )
            And count is reset to 1

            After the loop we again check if the last computed substring can be added, If count>1 again, We add it

            After that we return res+len(s) mod 10**9+7
            *Why add len(s)?
                We skipped all the single character cases (count>1 was only considered)
                Thus to consider them, We add len(s)
            
            That's it :coinflipper: ;)
        '''

        for i in range(1,len(s)):
            if (s[i]==s[i-1]): # Setting the count of chars in current homogeneous substring
                count+=1
            else: # Homogeneous substring ended
                if count>1:
                    res = res + count*(count-1)//2 # n(n-1)//2 is a pair formula which gives number of possible pairs
                count = 1 # count is reset
        if (count>1): # For the last substring which was left uncomputed after loop end
                res =res + count*(count-1)//2
            
        return ((res+len(s))%(10**9+7)) # You added all the homogeneous ones, But what about the single occurences? count>1 means you skipped all single occurences, Thus to count them we add len(s) which represents every single character once