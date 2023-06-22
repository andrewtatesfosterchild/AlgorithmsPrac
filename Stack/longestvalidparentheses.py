class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # Logic: Stack implementation

        '''
            We'll do this today itself in clear mind
        '''

        stack = [-1]
        max_val = 0

        for i,char in enumerate(s):
            if char =='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    curr_val = i - stack[len(stack) - 1] # Current index - stack's top pointer
                    max_val = max(curr_val,max_val)
        
        return max_val