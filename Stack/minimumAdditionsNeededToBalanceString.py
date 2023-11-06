class Solution:
    '''
        This solution entirely plays on the not matching left parentheses

        We start by itratiing through the string, When we encounter a left, We push it

        However, Things get tricky when we don't:

        Now , When we encounter a right parentheses,
        And on top of that the stack is empty, We are definitely missing one left parentheses to match the right open one, So count+1 and We push a left parentheses to compensate for it

        Now, We have an open right, If the next one in the string is an open right, We can pop this left out and skip the next character in the string as it forms a closed pair

        So we do exactly that
        if (idx < len(s) - 1 and s[idx + 1] == ')'): # Paired parentheses
                idx+=1 # If pair found we can skip next char
                stack.pop()
        
        However, If the next one is still not a closing parentheses,
        We are now missing a closing parentheses, So count+=1

        And idx +=1 to check the next element in the next iteration

        Now definitely has some of the answers but some are still in the stack,
        In the form of UNMATCHED LEFT PARENTHESES, Which require? TWO right closers

        so count+= len(stack) * 2
        return count

        That's it, Done

    '''
    def minInsertions(self, s: str) -> int:

        stack = list()
        count = 0
        idx = 0

        while (idx < len(s)):
            char = s[idx]
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    # We are missing an opening parenthesis
                    count+=1 # Count incremented
                    stack.append('(') # Filling in the left parentheses
                if (idx < len(s) - 1 and s[idx + 1] == ')'): # Paired parentheses
                    idx+=1 # If pair found we can skip next char
                    stack.pop()
                
                # Unpaired right parentheses
                else:
                    count+=1
                    stack.pop()
            idx+=1 # Common index +1

        
        return (count + len(stack)*2)