# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Logic: List traversal

        '''
            The intuition behind this problem lies in making two lists and joining them

            But slow down, We will do this, Not in a traditional way though
            We'll use pointers on the same list and not make different lists

            The main logic lies in exploiting the indices

            the first index is always odd, thus
            odd = head

            the second index is always even in LL (2):
            even = head.next

            Keep an evenhead for further joining
            evenhead = even

            Here the magic begins

            while even and even.next:
                odd.next = even.next 
                as we know every index after even is odd , "exploiting the index"

                odd = odd.next
                for basic traversal and for the setting of next even , since this odd's next will be the next even

                even.next = odd.next
                the currently set odd's next is the next even , "exploiting the index"

                even = even.next
                for basic traversal and for the setting of next odd , since this even's next will be the next odd
            
            odd.next = evenhead
            for setting the evens after the odd's tail

            return head
            returns all this mess we've made xD

            That's it, :coinflip:
            

        '''

        if not head:
            return None

        odd , even = head , head.next
        evenhead = even


        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenhead

        return head