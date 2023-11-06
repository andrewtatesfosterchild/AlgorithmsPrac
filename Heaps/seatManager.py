# Logic: Two queues? Two stacks? Pop pop?

'''
    The moment I saw this question, One thought comes into mind
    Two arrays, Unreserved and reserved
    That's it, Question over

    That's true, Nothing else is left in this question
    Just keep popping and appending according to the function calls

    Where you have to play now is,
    The moment you implement unreserved, You'll realise with the current method,
    The array needs to be sorted everytime.
    TLE due to bruteforcing
    The moment THIS happens, Understand that a priority queue will be used.
    This is a min-heap question

    And You actually need only one heap ;)
    That's it, Done, Cool


'''
class SeatManager:

    def __init__(self, n: int):
        self.available = list(range(1 , n + 1))
        heapify(self.available)

    def reserve(self) -> int:
        return heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available , seatNumber)


        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)