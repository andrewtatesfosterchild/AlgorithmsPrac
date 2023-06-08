class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        res = ""
        n = len(x)

        # Logic: The question says you have no environment to store 64 bit 'integers', But strings? ;)

        '''
            This is rather an interesting approach to solve this problem
            We use typecasting and string slicing to its ultimate potential

            firstly x is typecasted into str(x)
            res = "" for result obv
            n = len(x) (not needed obv)

            Next, We start appending into the result string by rev iterating over str(x)
            *What problem can it cause?
                If x is -ve, The - is treated as a char and appended at the end due to the rev for loop

            For this, After the appending loop, Check if res[-1] == '-':
                If yes, Perform basic string slicing
                    res = '-' + res[:-1]
            
            Now check if it falls in our range:
                int(res) if abs(int(res))<=(2**31-1)
                * why abs?
                    Negative values bozo -_- , Python modulus acts around negative values, Let's make our lives easier
                    by not using modulus at all first, And not using negative comparisions either

                    Note: You can even use math.fmod() to achieve the same result with mod of negative numbers

                    Thus, return int(res) if abs(int(res))<=(2**31-1) else 0

                    That's it :coinflipper: ;)


        '''

        for i in range(n-1,-1,-1):
                res = res + x[i]

        if res[-1] == '-':
            res = '-' + res[:-1]
        
        return int(res) if abs(int(res))<=(2**31-1) else 0