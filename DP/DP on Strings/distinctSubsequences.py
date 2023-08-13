class Solution:

    # Logic: Recursion + Memoization

    '''
        What was the primary instinct of this?
        Can we just calculate all the subsequences and return the count of the ones that matched?
        Okay we can do that, Infact we will do that, But we will use indices this time too

        Read the question carefully, It says distinct subsequences of S which equals T

        Seriously tf is up with indices in p up -_-
        The main logic this problem survives on is comparing indices
        Indices of what? Indices of s and t

        The base case seems pretty logical,
        If you are comparing indices of s and t, And you were able to reach the end of target,
        That's a successful hit, You've found a subsequence, Return 1

        On the other hand, If base case 1 fails and you've reached the end of s,
        return 0

        If you've already calculated for (idx_s , idx_t) somewhere,
        return that from self.visited

        Now, If two same chars are spotted s[idx_s] and t[idx_t], Explore further into this branch
            count+= self.helper(idx_s + 1 , idx_t + 1 , s , t)
        
        If the characters are different, Doesn't matter , Keep the target index there only na, We are matching subsequences, Might be the case where some other chars of s will become matching and complete the sequence later
        *Why increase index of s tho, why not of t?
        Here's where the beauty of this question lies, Attention to detail.
        Look again, The question says 'distinct subsequences of s which equals t'
        Consider an eg. s = bmag t = bag
        Start looking , b match , m & a mismatch , now if I increment s index, a and a match, g and g match, matched subsequence? cool

        count += self.helper(idx_s + 1, idx_t , s , t)

        Just memoize the result
        self.visited[(idx_s , idx_t)] = count

        return count

        That's it , Nothinig new , We've done this before

        Cool

        DP tables soon ;)
    '''
    def numDistinct(self, s: str, t: str) -> int:
        self.visited = {}
        return self.helper(0, 0, s, t)
    
    def helper(self, idx_s, idx_t, s, t):
        if idx_t == len(t):
            return 1
        if idx_s == len(s):
            return 0
        
        if (idx_s , idx_t) in self.visited:
            return self.visited[(idx_s , idx_t)]
        
        count = 0
        
        if s[idx_s] == t[idx_t]:
            count += self.helper(idx_s + 1 , idx_t + 1 , s , t)
        
        count += self.helper(idx_s + 1 , idx_t , s , t)

        self.visited[(idx_s , idx_t)] = count

        return count