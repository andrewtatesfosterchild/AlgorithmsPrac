class Solution:
    # Logic: Real shit DP begins here

    '''
        What I understood from this problem
        1. DP relies on past outcomes
        2. DP uses a DP array to store the past outcomes
        3. The only brilliance is how to utilize and set up this array
        4. Doesn't matter how trivial the result is, It will be used by the following outcomes so calculate it

        Was this so difficult? Not at all.
        The DP array is working like my brain, To solve this question, My brain calculates the amount of coins and stores it, Checking for the next combination possible. Although it is much faster, The process behind DP is the same. DP is your brain and DP array is your memory, Which stores all the possible outcomes and utilizes them later

        For each amount right from 0 to 11
        We store the minimum number of coins required to make that amount
        And in the process, We end up using the previous values straightforward. for dp[0] 0 coins are required, for dp[1] however dp[i - coin] + 1? What's this? i is 1 , coin is 1 , which makes? dp[0]! dp[0] is 0, dp[0] + 1 is 1, So we need a single coin of 1 to make the amount 1. That's how the past outcomes are affecting the future ones

        But why would you set an amount + 1 instead of amount?
        The primary reason for setting a value greater than the required amount is, All the combinatorics you do will result in a min amount
        That is LESS than amount + 1, So the dp array can always be updated
        But here's a catch , The DP array won't be updated EXCEPT when , The amount you're dealing with can't be formed at all with the given combination of coins

        The essence of DP is to develop conditions which can use past outcomes to make the present ones

        Let's talk after 100 questions xD

        That's it , Cool
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin , amount + 1):
                dp[i] = min(dp[i] , dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]
