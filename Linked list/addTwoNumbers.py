# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Logic: Reverse both lists, Add nodes and create new list, Return that list

    '''
        This problem is really f*cking good

        Addition takes place from least significant bits, The units place.
        This is why we reverse the lists, and then add them

        But again, Returning the list like this will return the reversed list, So we need a logic that fixes this whilst iterating and adding

        head = ListNode(carry)
        head.next = ans
        ans = head

        is exactly that logic

        Imagine adding two lists:

        l1 = [7,2,4,3]
        l2 = [5,6,4]

        reversed, They look like
        l1 = [3,4,2,7]
        l2 = [4,6,5]

        Now, lets declare some variables which are going to be used
        totalSum = 0
        carry = 0
        ans = ListNode()

        starting the loop,

        while l1 or l2: *We need to keep adding till the longest list has exhausted

            if l1: *l1 exists in this iteration
                totalSum+=l1.val
                l1 = l1.next
            if l2: *l2 exists in this iteration
                totalSum+=l2.val
                l2 = l2.next
            
            Now assign the value of totalSum to ans.val, but see this
            ans.val = totalSum % 10, IF this is a double digit number, I want only the units place to stay here, rest will be a carry... IF not, Simply just assign thr value

            Now simply carry = totalSum // 10 , This is basic addition bruh

            Now we start assigning

            ans.val = totalSum # Assigning the value

            head = ListNode(carry) # Creates a new node everytime with carry
                *Why with carry?
                *Specifically for the last added to have a node if it overflows
            head.next = ans # Points the node to the generated answer
            ans = head # Answer now points at head, Making answer the head


            **What we basically did here:
            1. We kept a node ready for the next iteration, since it assigns totalSum to ans.val, Meaning it will assign to the previously newly created node
            2. We are already mantaining the answer in the reversed order where returning ans will directly return the linked list in correct order
            3. The only time you WILL return ans however, IS when a carry is generated in the last bit addition, Meaning there is an overflow (The thing we worked out this logic for)
and it needs to be returned, So we return ans which WILL contain the carry
            4. Else, If not carry exists in the last addition, We return ans.next, which inevitably skips the overflow carry
            
            totalSum = carry # Keeping the carry already added to totalSum for next iteration

        return ans.next if not carry else ans

        That's it
        :conflip: :coinflip:
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l2 and l1:
            return l1
        elif not l1 and l2:
            return l2
        elif not l2 and not l1:
            return None
        carry = 0

        l1 = self.reversal(l1)
        l2 = self.reversal(l2)
        totalSum = carry = 0
        ans = ListNode()

        while l1 or l2:
            if l1:
                totalSum+=l1.val
                l1 = l1.next
            if l2:
                totalSum+=l2.val
                l2 = l2.next

            ans.val = totalSum % 10
            carry = totalSum // 10

            head = ListNode(carry)
            head.next = ans
            ans = head
            totalSum = carry
        
        return ans.next if not carry else ans
        
            
    def reversal(self , head):
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev