class Solution:
    # Logic: Subset combination problem ; Recursive processed unprocessed

    '''
        Looks complex, Is very simple

          def helper(self, p , up):
        if not up:
            list = []
            list.append(p)
            return list
        
        same approach, returns a list for not up

        digit = int[up[0]]
        i = (digit - 2) * 3 (since 1 is voicemail and mapping starts from 2, so (digit - 2)*3)

        if digit > 7:
            i+=1
        * Why? Because in the given keypad, 7 contains 4 letters
        len = i+3?
        This is the offset off all digit values
        Now if 7 or 9 is the digit
        offset has to be more than 3 (3 is generally for other keys)
        therefore, len+=1 for 7 or 9

        ans = []
        for i in range(i, len): # This is good, Idk how bu i in range i worked here
            char = chr(97 + i)

            ans.extend(self.helper(p + char , up[1:]))
        
        return ans

        Now its just about creating the list and extending it on every call

        That's it, Done, Easy



    '''
    def letterCombinations(self, digits):
        ans = self.helper("" , digits)
        return "" if ans[0]=="" else ans
    
    def helper(self, p , up):
        if not up:
            list = []
            list.append(p)
            return list
        
        digit = int(up[0])
        i = (digit - 2) * 3
        if digit > 7:
            i+=1
        len = i + 3
        if digit == 7 or digit == 9:
            len+=1
            
        
        ans = []
        for i in range(i, len):
            char = chr(97 + i)

            ans.extend(self.helper(p + char , up[1:]))
        
        return ans
        

        