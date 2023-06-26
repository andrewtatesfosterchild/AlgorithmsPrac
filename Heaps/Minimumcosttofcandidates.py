class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        # Logic: Heaps (Priority queues)

        '''
            Whenever a choice of selecting maximum or minimum from a group of elements is given, Always consider using Priority Queues

            In this problem, We first initialize two lists, head_workers & tail_workers,
            Since we need to consider first m candidates and last m candidates at a time only

        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):] * Why max(candidates , len(costs) - candidates)? Because there might arise a case where the candidates >= len(costs) - candidates, i.e. There are fewer elements in costs than candidates, So we have to append candidate elements to tail_workers, Otherwise len(costs) - candidates would do well


        This performs the appropriate slicing

        Now, To convert these lists into heaps,
        heapify(head_workers)
        heapify(tail_workers)

        ans = 0 will give total cost

        next_head & next_tail are the pointers which point to the potential elements to be pushed into respective heaps next

        Initiating the loop , for _ in range(k):

        if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]: 
            * This line is important, Remember this, Python always gives higher precedence to AND than OR, thus head_workers and head_workers[0] <= tail_workers[0] is evaluated first and then an OR is taken

            * But why if not tail_workers OR?
                Let's take a scenario where the costs available are less than the candidates, go back to the slicing tail_workers = costs[max(candidates, len(costs) - candidates):], SO, Isn't tail workers empty now? This condition flips to True and the condition executes anyhow, In simple senses, This is done to always prioritize extracting from head_queue first as a smaller index cost is preffered in case of equal costs of head and tail, Till head

            When the condition is defied , Else will be executed where tailqueue is utilized for cost extraction

            ans+= heappop(head_workers) self explainatory

            if next_head<=next_tail:
                heappush(head_workers,costs[next_head])
                next_head+=1
            
            pushing & incrementing

        else:
            ans+= heappop(tail_workers) self explainatory again

                if next_tail>=next_head:
                    heappush(tail_workers,costs[next_tail])
                    next_tail-=1
                
                pushing & decrementing
        
        Finally, return ans


        That's it, :coinflipper: ;)

        '''

        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]

        heapify(head_workers)
        heapify(tail_workers)

        ans = 0

        next_head = candidates
        next_tail = len(costs) - candidates - 1
        
        for _ in range(k):

            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                ans+= heappop(head_workers)
            
                if next_head<=next_tail:
                    heappush(head_workers,costs[next_head])
                    next_head+=1

            else:
                ans+= heappop(tail_workers)

                if next_tail>=next_head:
                    heappush(tail_workers,costs[next_tail])
                    next_tail-=1
        
        return ans