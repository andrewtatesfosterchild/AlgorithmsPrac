class Solution:
    def countPrimes(self, n: int) -> int:
        # Logic: Sieve of Eratothenes

        '''
            The most efficient way to find prime numbers in a range of n numbers

            Sieve of Eratothenes works only one one fundamental math principle:
                All the multiples of a prime number will never be prime themselves

            Thus, using this principle we can calculates the primes till n easily

            That's it, :coinflipper:


        '''

        if n == 0 or n == 1:
            return 0 # since they are not prime
        
        prime = [True]*n # Let me start with the hypothesis that everything I shall see is prime

        for i in range(2 , int(n**0.5) + 1): # Check till sqrt since factors beyond sqrt are not considered
            if prime[i]: # If prime is assumed to be true
                for j in range(i << 1 , n , i): # Flagging all the multiples as not true
                    prime[j] = False
        
        return sum(prime) - 2 # Subtracting 0 and 1 from case