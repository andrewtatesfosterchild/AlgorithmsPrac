class Solution:
    def lastSubstring(self, s: str) -> str:

        # Logic: Bruteforce approach ( Find and compare all sunstrings and give max )
        # O(n^2) complexity so TLE 
        # Gotta find an alternative

        max = "aaaaaa"

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]>max:
                    max = s[i:j]
                

        return max