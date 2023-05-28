class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1

        # Logic: Two pointer approach

        '''
            Pretty basic two pointer problem approach

            We are supposed to remove any same characters from suffix and prefix of string till there are none left, And then calculate the length of the remaining substring

            Now, We start with initializing the pointers
            As always i = 0, j = len(s) - 1

            starting with a while loop i<j and s[i]==s[j]:
            * Why s[i] == s[j]? We want two equal characters at prefix and suffix, i is prefix and j is suffix, As long as they are equal, continue this loop.
            * Now mind you, This condition only checks for entry i.e. Do we have equal characters or not?, The calculation of how many equal characters can be removed will be done inside this loop
            set a temp var t=s[i] # or s[j] as both are equal anyway

            Now while i<j again and s[i]==t,* Why? Because suffixes start at j
                i+=1 (skipping all the same characters from the prefix)

            Similarly, while j>=i again and s[j]==t,* Why? Because prefixes start at i
            * Why j>=i and not j>i?  If we set j>i, J will never intersect i
                So in conlusion we need atleast one =, either i<=j or j>=i
                Just for intersection of both pointers and to avoid wrong results or infinite looping
                j-=1 (skipping all the same characters from the suffix)

            Now this will repeat till all the same characters are gone

            Two cases can happen now

            either j<i: This means that all the leftover characters were equal and there's not a distinct substring produced, i.e. everything got removed
            thus, return 0 # 0 characters left

            else: That is not the case, We've got some distinct characters we would like to return
            thus, return j - i + 1 or len[i:j+1] any which ways you like
            * Why +1 in j - i + 1
            Okay, If you do j - i it gives you elements between i and j exluding j, but we want to include j in the length of substring, thus +1 is required

            That's it, :coinflipper: ;)
            



        '''

        while i<j and s[i]==s[j]:
            t=s[i] # or s[j] your wish, totally upto you

            while i<j and s[i]==t: # Skipping all same prefix characters
                i+=1
            while j>=i and s[j]==t: # Skipping all same suffix characters
                j-=1
            
        if j<i: # This means earlier suffix characters loop met i, This can only mean one thing, suffixes were all equal uptil prefixes, This means string does not have any different characters and everything got skipped, Thus return 0
            return 0
        else: # There were some distinct characters
            return j-i+1 # j - i = elements in between, + 1 includes j in them


