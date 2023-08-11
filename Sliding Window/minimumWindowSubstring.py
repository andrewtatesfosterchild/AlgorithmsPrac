class Solution:

    # Logic: Sliding window + Hashmap on steroids


    '''
        What was the primary intuition of this problem?
        Sliding window and a hashmap, Brilliant, Correct.

        But there's a catch, The question which bugged us here is, Comparing the hashmaps doesn't work here, Because other characters ARE allowed in the window. So, Figure out a solution where we can target the windows which contain all the letters provided in substring t.

        There's only one way to do this, A count variable. A count variable 'matches' which increases everytime you spot a new character X which is:
        1. Present in counter of T
        2. Not already accounted for i.e. hashmap[s[i]] < tCounter[s[i]]

        What's the point of 1.? Why can't we just add s[i] to hashmap regardless of its presence in t?
        Why would you? Don't worry about the window, The window will be managed by l and i, And we only need counts of elements in t, Including any other count will blunder our calculation. Also it is only because of this we won't pop when the value hashmap[s[l]] will be 0 , because it only contains characters in t!

        Hold on, Why the 2. Point?
        because the question says "including duplicates". Fair enough so why not include them all?
        because our logic says and the question doesn't "including duplicates not beyond what are present in substring t"

        perfect. Now we have the matches ready

        While the matches == len(t):
            We'll minimize the window to the obtained string ,and from there, To the min of subsequent windows to come

            Amazing, Now time to slide the window, hashmap[s[l]]-=1
            Now here's an important condition to understand again,
            if hashmap[s[l]] < tCounter[s[l]] , This means you took out a character which was supposed to be, For a valid subtring to exist.
                Therefore , matches-=1
            l+=1 # slide the window
        
        return window

        That's it , Was this so difficult? Have we not done the same question atleast 20 times?

        Cool
        



    '''
    def minWindow(self, s: str, t: str) -> str:

        tCounter = Counter(t)
        hashmap = {}
        l , window = 0 , ""
        matches = 0

        for i in range(len(s)):
            
            if s[i] in tCounter:
                if s[i] not in hashmap:
                    hashmap[s[i]] = 0
                if hashmap[s[i]] < tCounter[s[i]]:
                    matches+=1
                hashmap[s[i]]+=1

            
            while matches == len(t):
                if not window or i - l + 1 < len(window): # Important way of setting windows, Remember this
                    window = s[l:i+1]
                if s[l] in hashmap:
                    hashmap[s[l]]-=1
                    if hashmap[s[l]] < tCounter[s[l]]:
                        matches-=1
                l+=1


        return window