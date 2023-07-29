class Solution:
    # Logic: Using stack to keep a track of parentheses

    '''
        Actually an interesting problem,
        Remove the outermost parentheses, How can we do that?

        For starters , We know that the string has valid parentheses , So we need not worry about that.
        The only thing we need to keep an eye on is to remove all the outer parentheses and return all the inner ones

        We use a stack to do so, How? Let's see:

        The purpose of stack is to always hold atleast one outer parentheses, So that when it is popped out we know that an outer pair has been neglected

        For this purpose whenever the stack is empty, It means the next parentheses is going to be an opening '(' outer parentheses, Just simply append it to stack

        Now we start looking for the closing outer, but while carefully including the well formed inners:

        If an opening occurs and the stack is NOT empty, Means its an inner opening, append it to stack as well as res
        If a closing occurs , We pop the stack , And here's the magic
        If the closing was for an inner opening, The stack will not be empty on popping, As it is already holding an outer opening '(' , So append this inner closing ')' to res

        Now all that remains is the outer opening
        If another closing occurs, And we pop, The stack becomes empty indicating an outer pair was popped, So we neglect adding this ')' into the result as well.

        Stack is empty again so we append the next occuring character as outer opening,
        And the process continues till the string is finished

        That's it, So easy, What's so difficult in this?
    '''
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ""

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char == '(':
                    stack.append(char)
                    res+=char
                elif char ==')':
                    stack.pop()
                    if stack:
                        res+=char
        return res