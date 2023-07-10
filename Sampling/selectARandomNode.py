# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Logic: Fixed - Range Sampling

    '''
        To randomize the probability of finding something, sampling is used

        The main intution behind this problem was to select a random element from the linked list stored in an array, and return it

        So that's what we did :P

        Let's see how though:

        Inside the constructor we made a range array. This array stores the values of nodes for quick return in the latter half

        Let's now enter the getRandom():
        
        pick = int(random.random() * len(self.range))


        random.random()? WTF? 
        Yeah a python library function which returns a float val between 0 and 1.
        We made it int so it returns either 0 or 1

        Get it like this:
        random.random() : [0,1) floating val in this range
        random.random() * len(self.range) : [0,len(self.range)) range scales up to len of range
        int(random.random() * len(self.range)) : Truncates the decimal point and generates a number equivaluent to 0 to len(self.range) - 1, i.e. index of the range

        Now simply return self.range[pick]

        That's it, Done B)

        Note: There's an even better method, Although technical not intuitional called 'Reservoir sampling' which addresses unknown size and a constant space too!

        Check it out if needed: https://leetcode.com/problems/linked-list-random-node/editorial/

    '''

    def __init__(self, head: Optional[ListNode]):

        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        #Design an array
        #Use re.random number generator
        #Choose the index to be given

        pick = int(random.random() * len(self.range))

        print(pick)
        return self.range[pick]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()