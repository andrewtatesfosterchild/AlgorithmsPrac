class Solution:

    # Logic: Backtracking + Memoizatiion ; Classic DP problem

    '''
        The approach seems so complex at first, What is all this memo and return True everywhere?! O.o

        This is one of the most logical questions anyone can come across
        Really what are we donig here? We are just comparing everytime if the words in the dict are matching our string, THAT's IT!

        Now that you know what we are doing, Let's understand how we are doing it.

        We have 3 important parameters of this problem,
        s = the string of recursion calls, Initially the main string
        wordDict = list of given words
        memoization table = A hashmap which marks the routes already visited by the backtracking

        Let's enter helper:
        First thing it checks for is string, If string is empty return true

        Then it checks... Wait lets keep this part for later and get into the for loop action

        for each word in wordDict:
            check if the string starts with the word
            If it does, Good!
            create a suffix suffx = s[len(word):]
            Now we have the front part extracted, A word is gone
            if self.helper(suffix , words , memo): will make a recursive call
            And there again we check for empty string and visited path, If not any we again start the for loop and check for a match, If yes, We make the suffix and check for the match in the next recursive call

            But what if , The for loop check in the next recursive call fails, Then?
            We execute the code after the for loop, We marke memo[s] as false and return False
            Here, We memoized the string so that whenever we come across the same backtrack solution we will use it.

            A false is returned, Now what? Start backtracking, And try for a different match
            But what if all strings matched, Start returning true, Each path will be marked in memo as False after it is visited so that you cant visit it again, And we will have multiple solutions if they exist

            That's it , Done , Was this so difficult? Everything is repeated , Same
            Cool?

    '''

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if not s:
            return True

        if s in memo:
            return memo[s]

        for word in wordDict:
            if s.startswith(word):
                suffix = s[len(word):]
                if self.helper(suffix, wordDict, memo):
                    memo[s] = True
                    return True

        memo[s] = False
        return False
