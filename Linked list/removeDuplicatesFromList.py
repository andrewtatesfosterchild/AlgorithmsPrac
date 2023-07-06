# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Logic: As simple as it gets, LL traversal, Why is this problem marked medium -_-

        '''
            IDK WHAT TO SAY
            just keep checking the current val with the next val if same just temp.ext = temp.next.next or else if different temp = temp.next
        '''

        if not head or not head.next:
            return head

        temp = head

        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head