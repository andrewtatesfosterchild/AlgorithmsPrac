class Solution:
    def toLowerCase(self, s: str) -> str:
        # Logic: No isupper islower bs used, pure ASCII adjustment

        '''
            Tf is this res = res + chr((ord(s[i]) + (ord(s[i]) - 65))+(97 - ord(s[i])))???
            Let's break it down:
            1: chr(ord(...))
                Returns a chr for desired ord
            2. (ord(s[i]) ord value of capital letter
            3. (ord(s[i]) + (ord(s[i]) - 65)) ord value of capital letter plus the difference of odd val from captial 'A
            4. (ord(s[i]) + (ord(s[i]) - 65))+(97 - ord(s[i])) added with the difference of s[i] from small 'a' to jump till small 'a' and previous abjustment ensures that we get equivalent ascii character as of the capital 'A'
            

        '''
        res = ""

        for i in range(len(s)):
            if 65<=ord(s[i])<=90: # Condition to ensure no symbols are modified whatsoever
                res = res + chr((ord(s[i]) + (ord(s[i]) - 65))+(97 - ord(s[i])))
            else:
                res = res + s[i]
        return res