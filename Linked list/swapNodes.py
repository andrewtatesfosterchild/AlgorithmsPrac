# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Logic: Basic pointer logic

    '''
        No bro science, Just simple pointer play around LL

        Firstly we are asked to swap the kth node from the beginning and from the end

        So we traverse the LL till we reach the kth node from the beginning (and set the tail1 alongwith it)

        set the traversed temp ptr as swap1

        Now while temp ptr.next, keep setting tail2 , and swap2

        Now after this you have both swap1,swap2 and tail1,tail2 ready

        After this its just some case handling and then done

        if swap1 == swap2:
            both ptrs are equal, therefore do nothing and return head

        if not tail1:
            This means that k is 1, Thus tail1 was not set, And swap2 is the end node
            What to do here? Imagine, when swapped, Won't swap2 become the head?
            thus, head = swap2
            and when we set swap2.next = swap1.next, We get the whole list in order and we return the head
        else:
            tail1.next = swap2 , The standard linking
        
        if not tail2:
            This means k > the nodes present in the list, As ptr1 reached the end of the list
            It wont even bother entering while ptr1.next loop and thus tail2 will never be set, In such a case, just set head = swap1, as no swapping is possible
        else:
            tail2.next = swap1, The standard linking

        Now, For the next linking
        swap1.next , swap2.next = swap2.next , swap1.next

        That's it


    '''
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        ptr1 = head
        tail1 , tail2 = None , None
        for _ in range(k - 1):
            tail1 = ptr1
            ptr1 = ptr1.next
        
        swap1 = ptr1
        
        swap2 = head

        while ptr1.next:
            tail2 = swap2
            swap2 = swap2.next
            ptr1 = ptr1.next

        if swap1 == swap2:
            return head
        
        if not tail1:
            head = swap2
        else:
            tail1.next = swap2
        
        if not tail2:
            head = swap1
        else:
            tail2.next = swap1
        
        swap1.next , swap2.next = swap2.next , swap1.next

        return head