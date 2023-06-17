class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Logic : Binary division

        '''
            Binary division is one of the cleanest approaches to these kind of problems

            To start off, Check if the signs of the numbers are same, This will help in determining the sign of the result

            Next, We take abs values of dividend & divisor
                *Why? Because we're following the subtraction aproach and abs values make life easier

                res = 0 initially

                Then, Starts the magic ;)

                Two loops, Why two loops !?
                    Imagine a case where dividend = 35, divisor = 3

                    let's do it with only inner loop i.e. while dividend >= temp=3 (i is set to 1)
                    dividend -= temp
                    res += i
                    i <<= 1
                    temp <<= 1

                    After Iteration 1:

                        dividend: 32
                        res: 1
                        temp: 6
                        i: 2

                    After Iteration 2:

                    dividend: 26
                    res: 3
                    temp: 12
                    i: 4

                    After Iteration 3:

                    dividend: 14
                    res: 7
                    temp: 24
                    i: 8

                    Break off at iteration 3 due to exponential multiplication

                    But is dividend<divisor yet? We failed ;)

                    Now try with two loops where outer loop is while dividend>=divisor,
                    That's the logic behind two loops

                Alright wizardry over, now determine the sign of result
                if not positive:
                    res = -res
                
                And then , Remember this overflow comparision, Very efficient and imp

                return min(max(-2**31,res),2**31 - 1)

                That's it, :coinflipper: ;)





        '''



        positive = (dividend < 0) is (divisor < 0) # Checks if dividend & divisor have the same sign

        dividend , divisor = abs(dividend) , abs(divisor) # dealing with positive numbers only

        res = 0
        
        while dividend >= divisor: # Outer loop which keeps the division going if inner loop breaks
            temp, i = divisor, 1 # Sets temp = divisor and i = 1 each time

            while dividend >= temp: # Inner loop which is bound to break earlier due to binary division, the temp grows exponentially and breaks the loop earlier
                dividend -= temp
                res += i
                i <<= 1 # Left shift bitwise multiplication
                temp <<= 1 # Left shift bitwise multiplication

        if not positive: # if signs were not equal
            res = -res
            
        return min(max(-2**31,res),2**31 - 1) # goated overflow comparision