# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Logic: Partitioning a List = Forming two lists

        '''
            What does your intuition say when you read this question?

            Obviously we'll need two parts of the list

            So that's what we'll do, Make the two parts, The smaller and the larger one

        smallerList = ListNode()
        largerList = ListNode()

        These two are the two list pointers

        smallerHead = smallerList
        largerHead = largerList

        These other two are for the head pointers of the defined lists

        Time to traverse the main list and attach results to these LLs

        while head:
            if head.val < x:
                smallerList.next = head
                smallerList = smallerList.next

            if the val is smaller, we attach it to the smallerList and move forward in the list

            else: (> or = cases)
                largerList.next = head
                laergerList = largerList.next

                similarly if the value is greater or equal , we attach it to the largerList and move forward in that list
            
            head = head.next

            moving head of the main list to check the next value

        Now after the loop, Let's access the situation

        We have:
            Two head pointers, pointing at smaller and larger lists
            Two tail pointers, Which were actually smallerList and largerList before the loop

            Now I have to do only one thing, attach the tail of the smaller list to the head of the larger list

            For that,
            largerList.next = None

            setting next of the larger LLs tail to None

            smallerList.next = largerHead.next

            attaching the largerHead's following nodes to the smallerList's next

            return smallerHead.next

            That's it, Question over

            Follow the Orcam's Razor ;)


        '''

        if not head or not head.next:
            return head
        
        smallerList = ListNode()
        largerList = ListNode()

        smallerHead = smallerList
        largerHead = largerList

        while head:
            if head.val < x:
                smallerList.next = head
                smallerList = smallerList.next
            else:
                largerList.next = head
                largerList = largerList.next
            
            head = head.next
        
        largerList.next = None
        smallerList.next = largerHead.next

        return smallerHead.next