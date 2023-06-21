class Solution:

    def minCost(self, nums: List[int], cost: List[int]) -> int:

        # Logic: Binary search, v.imp intuition for standard problems like this

        '''
            Refer this https://leetcode.com/problems/minimum-cost-to-make-array-equal/editorial/, It's a bit mathematical but brilliantly explains the intuition behind such problems being solved by binary search 
            Let's talk about get_cost function,

            get_cost finds the cost of converting each array element into the given base element

            Breakdown of this line: return sum(abs(base - num)*c for c,num in zip(cost,nums))
                abs(base - num)*c is an expression which calc the total cost incurred to change one element of array to the desired base element 
            
                for c,num in zip(cost,nums), This just forms the iterable for summation
            
            Next is initializing answer immediately, since array can have only 1 element too and later this can become an edge case (Remember this, It's an important standard for any other problem)

            answer = get_cost(nums[0])

            The upper & lower bounds are given by:

                s = min(nums)
                e = max(nums)
            
            *Why? Because the minimum cost is bound to exist within these values

            start the while loop and get cost_1 and cost_2 by:

                cost_1 = get_cost(mid)
                cost_2 = get_cost(mid+1)
            
            Update answer

                answer = min(cost_1,cost_2)
            
            Now, Here comes the intuitive part, And to be fair, This is very similar to the dangling speed search of the Koko eating bananas problem, so refer that too

            if cost_1 > cost_2:
                s = mid + 1
            else:
                e = mid
            
            Wait what wtf happened? O.o

            Let me explain:
                Remember the bounds? s = min(nums) e = max(nums)

                Imagine mid is calculated, Now consider that the cost remains the same anyhow

                Therefore, Cost is constant, The only thing variable is the base element which is given by mid
                If the cost_1 > cost_2:

                    This means that the base element is too less and it takes more cost to change everything to mid, Thus by moving s to mid + 1, We are actually going towards upper bound which will increase the base element too, Thus moving into the correct search space

                    On the other hand, cost_1 <= cost_2:

                    This means that the base element can give the mimimum cost, But there might be smaller elements that might give the minimum cost. Thus e = mid, Which narrows search space till e = mid, Thus decreasing the base element and moving to the correct search space

            After this? Just return answer

            That's it, :coinflipper: ;)

        '''

        def get_cost(base):

            return sum(abs(base - num)*c for c,num in zip(cost,nums))

        answer = get_cost(nums[0])

        s = min(nums)
        e = max(nums)

        while s < e:
            mid = s + (e-s)//2

            cost_1 = get_cost(mid)
            cost_2 = get_cost(mid+1)

            answer = min(cost_1,cost_2)

            if cost_1 > cost_2:
                s = mid + 1
            else:
                e = mid
        
        return answer