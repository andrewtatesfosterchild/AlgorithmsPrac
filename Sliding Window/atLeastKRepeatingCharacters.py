class Solution:

    # Logic: Sliding window on steroids

    '''
        At first, this looks like a peasant's problem , But this is actually a good question

        What do I have to produce?
        Give me the maximum length of the subarray where atleast k repeating characters occur

        Find instinct should always be clear, Subarray means sliding window and frequency means hashmap

        Okay sherlock, What's next?
        To find repeating characters, we first need the unique elements in the string
        Python makes life easier as maxUnique = len(set(s))

        Now what exactly will I use this for?
        We are going to do something very clever, We are going to group the windows 1 by 1, right from the count of uniques starting from 1 and going on till maxUnique

        In other words, We will look for the longest string of letters where each letter repeats atl east 1 , then 2 , then 3 and son on... times

        This ensures all the windows are covered

        In each group , You initialize these variables
        hashmap = [0] * 26
        windowstart , windowend , idx , unique , countatleastk = 0 , 0 , 0 , 0 , 0

        hash of 26 due to 26 alphabets

        Now, while windowend < len(s):
        if unique <= currUnique:
            More uniques can be found, expand the window
            idx = char's ascii - 97

            Then its just hashmap play
            It hashmap[idx] is zero unique+=1
            then hashmap[idx]+=1
            If hashmap[idx] == k: countatleastk+=1

            windowend+=1
        
        # Now when enough uniques in this group are found, start shrinking the window
        else:
            calculate index for windowstart again

            hashmap[idx] == k? countatleastk-=1
            hash idx -=1
            if hash idx 0
            unique-=1

        Now just compare if unique = currunique and unique = countatleastk
        res becomes max of all the windowlens from this group


        That's it , Let's talk after 100 sliding window questions xD



    '''
    def longestSubstring(self, s: str, k: int) -> int:
        maxUnique = len(set(s))
        res = 0

        for currUnique in range(1 , maxUnique+1): # We will check unique elements of all counts, starting from 1 to max uniques

            hashmap = [0] * 26
            windowstart , windowend , idx , unique , countatleastk = 0 , 0 , 0 , 0 , 0

            while windowend < len(s):
                # Expanding the window till unique != currUnique
                if unique <= currUnique:
                    idx = ord(s[windowend]) - 97 # To find the respective index of this letter

                    if hashmap[idx] == 0:
                        unique+=1 #  A unique char is found
                    hashmap[idx]+=1
                    if hashmap[idx] == k:
                        countatleastk+=1
                    windowend+=1
                
                # unique elements > currUnique range, Shrink the window
                else:
                    idx = ord(s[windowstart]) - 97 # any char - ord(a) = index of that char in range 0 to 25

                    if hashmap[idx] == k:
                        countatleastk-=1
                    hashmap[idx]-=1
                    if hashmap[idx] == 0:
                        unique-=1
                    windowstart+=1
                
                # Determining whether to add current window or not

                if unique == currUnique and unique == countatleastk:
                    res = max(res , windowend - windowstart)
        return res