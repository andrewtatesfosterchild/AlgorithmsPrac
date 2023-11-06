# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Logic: Linked list ; Plain old linked list

    '''
        There was nothing new, Every step is the same as before

        Only thr brains you need is a slight on the edge

        What was the intuition, The single intuition which could have finished this question in seconds?

        "I see a reverse hidden somewhere" , That was the intuition

        Now look at the question again, And try reversing the list from the middle to the end

        And when you alternately link the nodes of these two lists, You will get the anser

        Don't ask me how to find the middle you already know it,
        Slow fast pointer

        Don't ask me how to reverse a link list, You already know
        prev curr method

        Don't ask me  how to perform alternate linkage, You already
        know basic linkedlist knowledge

        That's it , Was it something hard? Was it so difficult? Was it something that we have never done before? That's it, Done.
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow , fast = head , head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now slow is at middle

        rev = self.reverse(None , slow.next)

        slow.next = None

        while rev:
            next = head.next
            head.next = rev
            head = rev
            rev = next


            
    def reverse(self , prev , curr):
        while curr:
            next , curr.next , prev  = curr.next , prev , curr
            curr = next
        
        return prev