# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        Stack is a LIFO structure ; Use this property

        LL becomes reversed when put in stack,
        Pop every val and chec kwhile traversing if equal, true else false
        That's it
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head.next: # Single element is a palindrome
            return True

        stack = list()

        temp = head

        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        print(stack)
        
        while head.next: # We go till the end , Not till it is None , Can't check the value of None
            if stack[-1] == head.val: # Reversed order checking with head
                stack.pop()
                head = head.next
                continue
            else:
                return False
        
        return True
            
            
