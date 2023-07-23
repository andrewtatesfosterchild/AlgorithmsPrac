class Solution:

    # Logic: Permutation ; Recursive subset problem

    '''
        What amazes me is that there's absolutely no glory in these questions, These questions are all one and the same, They belong to the same subquestions.

        What's new in this, This is good old permutation
        Duplicates added? Hell to it, Do permutations with duplicates

        See one of the ways is to do it directly, Without planting a recursion for it

        Just perform the permutations and filter out the result later on using iteration

        But the thing is this approach is barely good enough, It is not very optimal keep that in mind, So lets plant something inside recursion

        By something, I mean backtracking

        Here, We use an external reference object res and append our backtracking results to it

        For unprocessed we are using the counter nums hashmap to keep a track of all the numbers being repeated

        Rest all is core backtracking procedures

        That's it, This is optimal
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
           #     ### Sub Optimal approach ###
    #     res = self.helper([] , nums)

    #     # res.sort()
    #     # prev = None
    #     # seen = []
    #     # for perm in res:
    #     #     if perm != prev:
    #     #         seen.append(perm)
    #     #     prev = perm
    #     # return seen

        
    
    # def helper(self , p , up):
    #     if not up:
    #         return [p]
    #     ans = []

    #     for i in range(len(p) + 1):
    #         f = p[0:i]
    #         s = p[i:]

    #         ans.extend(self.helper(f + [up[0]] + s , up[1:]))
        
    #     return ans

        res = []

    
        def helper(p , up):
            if len(p) == len(nums):
                res.append(list(p))
                return

            for num in up:
                if up[num] > 0:
                    
                
                    up[num] -= 1 # Backtracking start
                    p.append(num)

                    helper(p , up)

                    # Here, I'll revert the backtrack changes for other calls to function properly
                    p.pop()
                    up[num]+=1

        helper([] , Counter(nums))

        return res