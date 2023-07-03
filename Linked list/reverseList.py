# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Logic: Reverse links in a series, Imp standard question

        '''
            That's it , The intuition is only that much
            Take 3 pointers prev curr and next
            keep setting next as curr.next
            and reverse the links of curr.next as prev and prev = curr

            There's nothing more in this question but intuition

            Also, Why  while curr: and why not  while curr.next: ?
                Because the head link needs to change too, and curr.next stops at head, So the head will never be linked to the prev list, That's it

            :coinflip: :coinflip:
        '''

        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr:
            next = curr.next # Preserving the curr.next for further traversal
            curr.next = prev # Linking the next of the curr to the prev element
            prev = curr # Setting prev as curr for the next iteration
            curr = next # Setting current as next for the next iteration
        
        return prev # At the end prev points towards the last element which inturn becomes the new head of the linked list