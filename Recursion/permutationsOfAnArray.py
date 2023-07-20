class Solution:

    # Logic: Subset problem ; Recursive permutation

    '''
        This is just a recursive permutation algorithm ; similar to that of strings

        processed and unprocessed parts remain the same
        What changes?
        For permuations, You take everything ,There's no take / not take

        So why are the recursive calls increasing with the increase in p's length
        One logical and brilliant reason I'd say,

        "With each character increase in p, A possible position for a new character also increases , Thus it is always len(p) + 1 limit looping"

        if up is empty:
            you found a possible permutation,
            make a list and append it
            return this list to the previous call

        The previous calls keep extending the main answer and return th ans

        final answer is returned in a ans list like:
            ans = self.helper([] #processed, nums #unprocessed)
            return ans

        Also also notice one more thing, In this there's already an array provided thus you can simply mark up[i] instead of taking a char for it, Like we did in strings

        That's it

    '''

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = self.helper([], nums)
        return ans

    def helper(self, p, up):
        if not up:
            res = []
            res.append(p)
            return res

        ans = []
        for i in range(len(up)):
            f = up[:i]
            s = up[i+1:]
            ans.extend(self.helper(p + [up[i]], f + s))

        return ans
