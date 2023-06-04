class Solution:
    def numSub(self, s: str) -> int:
        # Logic: Good question, String split & Search

        '''
            This problem is a classic example of how important string splits can be.

            Approach we will follow:
            Firstly, To keep it as simple as possible, split the string at 0's
            And store this result in substrings

            Next, We start iterating over these substrings:
                1. We skip whitespaces produced by single 0's
                2. After that, We know all the rest contain 1's. So, The count of 1's can be given by len(substrings[i])
                3. Just do res = res + len(substrings[i]) * (len(substrings[i]) + 1)//2
                4. If the reult is too large for an int, modulo it by 10**9 + 7 and return
            
            That's it :coinflipper: ;)

        '''
        substrings = s.split('0')
        res = 0

        print (substrings)

        for i in range(len(substrings)):
            if substrings[i]!='':
                res = res + (len(substrings[i]) * (len(substrings[i])+1)//2)
   
        return res % (10**9 + 7)

        
        

        

        
                
