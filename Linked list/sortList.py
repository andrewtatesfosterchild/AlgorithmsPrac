class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Logic: Recursive Mergesort

        '''
            This is a standard problem and this is one of the best standard approaches to solve it aka the recursive mergesort on a LL

            The important points to focus upon are:
                1. The base case which returns head on the event of head being the only node present
                2. Two pointers approach which helps to find the middle node in the list
                3. The recursive calls
                4. The merging logic
            
            Base case is pretty self explainatory

            When we come to 2P approach, Fast pointer covers twice the distance as slow pointer does, Naturally slow ends up at the mid when fast reaches the end

            After that, we assign slow.next as mid and break the link between the list
            slow.next = None

            Then the recursive calls to repeat the entire process again
            left = self.sortList(head)
            right = self.sortList(mid)

            We move on to the merging logic
            dummy = ListNode()
            curr = dummy

            while left and right:
                Just keep comparing each value of left and right and keep connecting it to curr, and traverse to the next of whichever is connected in current iteration
            
            At last, One value should remain which is not none
            connect it with curr.next = left or right whichever is not none

            return dummy.next

            That's it
        '''

        if not head or not head.next: # Base case when only a single node exists in linked list
            return head

        
        slow , fast = head , head.next


        # Imp logic to find middle nodes in a linked list , fast slow pointer approach
        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next
        
        mid = slow.next

        # Disconnecting rest of the list to create two halves
        slow.next = None

        # Recursive calls
        left = self.sortList(head)
        right = self.sortList(mid)

        # Actual sorting
        dummy = ListNode()
        curr = dummy

        # Merging of sorted lists
        while left and right:

            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            
            curr = curr.next
        
        # Adding any remaining node (whichever is not None) 
        curr.next = left or right

        return dummy.next