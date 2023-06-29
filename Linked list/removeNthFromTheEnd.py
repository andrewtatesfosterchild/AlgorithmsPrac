# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Logic: Two pointers

        '''
            The idea is to remove the nth final node, The nth node from the last node of the linked list

            There are two ways to go about it

            Either I skim through the entire list and then calculate the nth node, Which will definitely lead to two passes

            Or I maintain two pointers, as in this approach

            Both the pointers atart from head

            The idea is to increment fast till n first

            If in the process fast becomes NULL, This means that the linked list does not have n nodes, So we return head.next, Thus removing head

            Else everything is fine and we have fast pointing to the nth node of the list
            But mind you we need to reverse the nth node from the end not the nth node from the beginning, The one where fast is pointing currently
 
            Now heres' the magic, We'll traverse the slow and fast pointers parallelly till fast.next != NULL, 
            When the fast pointer finally reaches the last node, the slow pointer would have moved n positions from its initial position. Since there is a gap of n nodes between the fast and slow pointers, this means the slow pointer is now exactly at the node right before the nth node from the end.

            Now simply slow.next = slow.next.next

            Return head

            That's it ;)
        '''
        
        fast = slow = head # Two pointers

        for i in range(n): # Traversing till nth node from the beginning
            fast = fast.next 
        
        if not fast: # Indicates is beyond length of list
            return head.next 
        
        while fast.next != None: # Traversing slow and fast parallely, mantaining a difference of n nodes
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next # deleting the nth node from the end

        return head