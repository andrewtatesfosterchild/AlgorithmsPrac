def zerochecker(n , count):
    if n == 0:
        return count
    
    rem = n % 10

    if rem == 0:
        return zerochecker(n//10 , count+1)
    
    return zerochecker(n//10 , count)

def numberofzeros(n):
    count = 0
    return zerochecker (n , count)

print (numberofzeros(1001))


    