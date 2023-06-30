# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Logic: Two pointer swapping

        '''
            Place a dummy node before the head node
            Make a prevnode point to dummy and currnode point to head

            To swap nodes:
            prevnode.next = currnode.next
            currnode.next = prevnode.next.next
            prevnode.next.next = currnode

            prevnode = currnode
            currnode = currnode.next


            That's it, :coinflip: ;)
        '''

        if (not head or not head.next):
            return head

        dummynode = ListNode()
        prevnode = dummynode
        currnode = head

        while (currnode and currnode.next):
            prevnode.next = currnode.next
            currnode.next = prevnode.next.next
            prevnode.next.next = currnode

            prevnode = currnode
            currnode = currnode.next

        return dummynode.next # Since head is lost and dummynode.next = HEAD
    