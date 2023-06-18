# # 3 approaches

# # Approach 1 : String conversion

import math

def reverse(n, i , j):
    if i >= j:
        return n
    
    n[i] , n[j] = n[j] , n[i]
    return (reverse(n, i+1, j-1))

n = 1317

res = reverse(list(str(n)), 0, int(math.log10(n)))

print(int(''.join(res)))

# Approach 2: normie modulo with external var for noobs

sum = 0

def reverse(n):
    global sum
    if n % 10 == n:
        sum = sum*10 + n%10
        return
    sum = sum*10 + n%10
    reverse(n//10)

reverse(1317)
print(sum)

# Approach 3

# For ppl who understand helper funcn B)

import math

def helper(n , digits):
    if n % 10 == n:
        return n
    rem = n % 10
    return rem * int(math.pow(10, digits - 1)) + helper(n//10, digits - 1)

def reverse(n):
    digits = int(math.log10(n) + 1)
    return helper(n , digits)
    
print(reverse(125))
