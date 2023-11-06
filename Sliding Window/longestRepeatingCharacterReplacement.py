class Solution:
    # Logic: In frequency questions perform sliding window on hashmap

    '''
        This question should have triggered one intuition
        To check for characters replaced , I have to check for the difference , Of what idc but a difference

        Second intuition click should have been:
        The highest frequency character stays
        # Why so? Would it be wiser to let the higher one stay and replace the already lower one , or to replace it to make the lower one dominant? Think about it.
        The lower frequencies have to be replaced

        How can I find the characters replaced in a span?
        If I subtract the size of the span with the maximum frequency of character observed so far, I'll get the characters to be replaced

        Now I'm given an upper bound k, Which restricts me to replace characters beyond k

        So, Combining the primary instinct and the secondary intuition, I get:
        I have to find the Difference between the current span and the max frequency of any character in the current span.

        This will give me the characters replaced in that span

        Once I have that , I'll just compare it with k,
        If <= k, I'll update my windowsize

        If > k, 
        I'll decrease the count of left character from the hashmap, and even pop it if its 0

        That's it

    '''
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        windowsize = 0

        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 0
            hashmap[s[r]]+=1

            # Characters replaced = characters processed so far - Highest frequency character   

            if (r - l + 1) - max(hashmap.values()) <= k:
                windowsize = max(windowsize , r - l + 1)
            
            else: # More characters are being replaced currently , Reduce them

                hashmap[s[l]]-=1
                if hashmap[s[l]] == 0:
                    hashmap.pop(s[l])
                l+=1
        
        return windowsize