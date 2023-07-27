class Solution:
    # Logic: Sliding window on Steroids + Set

    '''
        The problem was simple , The way we were solving it earlier was not, The memoization of checking for cards[j] in the whole previous window is o(N) in itself for larger cases atleast
        
        We used set just for memoization as duplicates prevented and search time is reduced
        
        Let's see how it works
        We start with i , j set to 0, Our two pointers
        
        Till you don't get a duplicate card keep adding those cards to a set and incrementing j
        
        When a duplicate card is found , else case gets executed
        and we try to remove this cards[j] element from set, Using a while loop and incrementing i
        While simulaneously minimizing the window size
        
        When the element is finally removed, The window size is already set
        
        just return this window size if it i not inf, else return -1
        
        That's it, Done   
    '''
    def minimumCardPickup(self, cards: List[int]) -> int:
        i , j = 0, 0
        windowsize = float('inf')
        seen = set()
        
        while (j < len(cards)):
            if cards[j] not in seen:
                seen.add(cards[j])
                j+=1

            else:
                while (cards[j] in seen):
                    windowsize = min(windowsize , j - i + 1)
                    seen.remove(cards[i])
                    i+=1
        
        return windowsize if windowsize != inf else -1