import math

# Get the integer reverse logic in your head, its imp

def reverse(n , digits):
    if n == 0:
        return 0
    
    rem = n % 10

    return rem * 10**(digits-1) + reverse(n//10 , digits - 1)


def palindrome(n):
    digits = int(math.log10(n)+1)
    return (n == reverse(n , digits))

print (palindrome(51115))
