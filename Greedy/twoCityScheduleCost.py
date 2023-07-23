class Solution:
    # Logic: Greedy approach

    '''
        Yes, This can be solved through DP too,
        But what's so greedy in this?

        Without sorting there's no greedy, Since the prices are randomized

        But what if I can sort them according to the difference of both flights? That's precisely what we do

        After that we can jut select the half of cheapest A's and half of cheapest B's

        Okay but, How is it woorking?
        Let me tell you how,

        When we sort them according to the difference between A's and B's, Now I want you to empty your mind and think about one and only one thing, When will the difference between two numbers be minimum?
        That's right, when first number is drastically smaller than the second number
        So thats what we will do, Half of the passengers who go to A will get the tickets in the first half of array, Since it IS the cheapest, that we just proved. And the rest half can take a ticket for B in the second half of the array, Since the second half will contain the smallest of B according to our sort & logic

        That's it, Done
        Code it anyway you want, The output matters

    '''
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key = lambda x:(x[0] - x[1]))
        sum = 0
        n = len(costs) // 2

        for i in range(len(costs)):
            if i < n:
                sum += costs[i][0]
            else:
                sum += costs[i][1]
        
        return sum


        