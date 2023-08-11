class Solution:

    # Logic: classic DP sum

    '''
        This is EXACTLY same as coin change, It's just that now you don't need to find the minimum denomination of coins to make up the amount. Instead, Give me the combinations which can make up the amount. So, What's changed? The loops still function the same , Because at the end we are dealing with coin change. So what's changed?!

        dp[0] = 1
        Why? There's always 1 way to make the sum 0 , Not taking any coins

        dp[i] does not represent the amount anyomre, It represents the combinations that can make up our final amount
        So dp = [0] + [amount+1]*amount
        changes to
        dp = [0]*amount+1 , Since initially 0 combinations for all of the i amounts

        The last change,
        dp[i] += dp[i - coin]

        This has the essence of the problem within it. DP keeps summing up the combinations previously formed by the previous coins and amounts. At the end, dp[amount] contains all of the pssible combinations made by all coins and amounts combined/

        return dp[amount]

        That's it, Was this difficult? No

        Cool , That's it

    '''
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1) # 0 ways to make up an amount initially
        dp[0] = 1 # 0 can be always made with no coins

        for coin in coins:
            for i in range(coin , amount + 1):
                dp[i] += dp[i-coin] # Summing up combinations of previous coins

        return dp[amount]