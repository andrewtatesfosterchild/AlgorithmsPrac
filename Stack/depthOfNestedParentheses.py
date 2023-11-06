class Solution:
    # Logic: Stack to find depth?!

    '''
        Stack is used whenever you will need a past result in the future, Or whenever you need maximum up till or result up till something

        Only catch here was when to calculate depth, and the answer was whenever you dont encounter a parentheses, Is that the only answer though? Sure It will give you the maximum result, But will it work for the case when where is no character in the string? It won't.
        
        Thus , The depth is computed twice , When inserting a parentheses into the stack, So to handle depth of cases like "()" , And once more if the element encountered is a character

        That's it
    '''
    def maxDepth(self, s: str) -> int:

        stack = []
        depth = -1

        for char in s:
            if char == '(':
                stack.append(char)
                depth = max(len(stack) , depth) # Opening parentheses depth
            elif char == ')':
                stack.pop()
            else: # Character encountered , Measure the depth till now
                depth = max(len(stack) , depth)
        
        return depth