# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Logic: LL Traversal is getting advanced

        '''
            It's all in the traversal when it comes to LLs

            Listen carefully, What we have to do is remove the duplicate elements and alongwith it the original element which has been duplicated

            Removing duplicates is easy, but what about the originals? That'll require some traversal technique

            But you must understand the basic intuition behind this, I will skip the elements till next.val is not a duplicate and link it to the previous non duplicate

            Let's start,

            if not head or not head.next:
                return head

            basic case, nothing new just returning if a single element or nothing is provided

            prev = ListNode()
            prev.next = head

            curr = prev

            prev holds the head of the linkedlist
            curr will be used in iterations ahead

            while curr.next and curr.next.next: This while loop condition is to ensure no errors occur in traversal

                if curr.next and curr.next.val == curr.next.next.val:
                    var = curr.next.val

                Here, the fun begins. we compared the next element to its next element, If the value is same, It is a duplicate and we stored the duplicated value in a variable called var

                 while curr.next and curr.next.val == var:
                    curr.next = curr.next.next
                
                This was the logic, That's it. The question is already over

                Hit your walnut brain hard,
                What's happening here?
                We are comparing curr.next with the var,
                Everytime its equal we make curr.next to curr.next.next,
                The while loop checks again if curr.next is val, If it is then again it links curr.next to curr.next.next and again will it be compared, and again will it be skipped till the duplicate element is lost

                What's after this? Nothing :/
                The further iterations will get rid of all duplicates

                one else case
                else:
                    curr = curr.next
                    To handle when curr.next is in fact not equal to curr.next.next

                That's it, Question gone

        '''
        
        if not head or not head.next:
            return head

        prev = ListNode()
        prev.next = head

        curr = prev

        while curr.next and curr.next.next:
            if curr.next and curr.next.val == curr.next.next.val:
                var = curr.next.val

                while curr.next and curr.next.val == var:
                    curr.next = curr.next.next
            else:
                curr =curr.next
        
        return prev.next