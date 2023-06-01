class Solution:
    def isNumber(self, s: str) -> bool:
        # Logic: Leetcode "HARD" this is, Ladies and Gentleman

        '''
            try excepts can work like clockwork in validity check questions like this one for instance

            In try, we check the following:
                if 'inf' in s.lower():
                    Dont need inf in string, testcases have it for some reason
                    return False
                s.isalpha():
                This condition evaluates if there are only alphabets in string
                    Return False if True
                
                *float(s) => The horsepower of this code
                Why?
                    Any valid number, whether it be decimal, non-decimal can be converted into a float value
                    If I'm facing any issue such as ValueError or TypeError or something else
                    That means I'm dealing with an invalid number
                
                Thus, The try returns True if float(s) works

                else it enters except and returns False from there

                That's it :coinflipper: ;)

        '''

        try:
            if 'inf' in s.lower() or s.isalpha():
                return False
            float(s) # Hero of the code
            return True

        except:
            return False