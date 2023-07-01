# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Logic: Simple and intuitive rotation

        '''
            In this problem the only thing that's important is intuition

            First things first, as all rotation problems k%len(elements) is a mandate to avoid overwork and the first while loop traverses and counts the list nodes well (count = 1 so as to count the head as well)

            then to start the loop
            The only two things that need to change:
                The tail link to head
                Tailprev link to None
            Rest everything remails the same
            
            Alongwith this, Everytime tail becomes new head and that's it, There's nothing more in this question

            while tail.next:
                tailPrev = tail # Stops one element before tail i.e. tailPrev
                tail = tail.next

            Important traversing technique to find the prevnode of a node

            That's it, :coinflip:

            
        '''

        if (not head or not head.next):
            return head

        temp = head
        count = 1

        while temp.next:
            count+=1
            temp = temp.next

        k = k%(count) # Reducing the effort
  
        for _ in range (k):
            tail = head 
            tailPrev = None

            while tail.next:
                tailPrev = tail # Stops one element before tail i.e. tailPrev
                tail = tail.next
            
            tail.next = head # Linked to head
            tailPrev.next = None # tailPrev becomes tail technically
            head = tail # head is now tail
        
        return head