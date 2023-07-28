# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Logic: Tortoise Hare / Slow fast / Floyd's Cycle detection algorithm

    '''
        Imagine a racetrack , If hamilton is racing at half the speed of Max Verstappen, Max is bound to meet Hamilton over the next lap at some point of the track

        Same logic applies here to the fast slow pointers, If slow pointer traverses at half the speed of fast pointer , They will meet at some point , And that point will be the start of our cycle

        We are supposed to return start of the cycle

        slow = head
        fast = head

        Both pointers start at head

        While fast and fast.next:
            fast jumps twice
            slow jumps once

            If both are equal , break the loop , a cycle exists

        else:
            return None , No cycle exists (while condition failed meaning fast reached end)

        Now , We are supposed to find the start node of a cycle , i.e. the node where the tail of the cycle points to

        For this, We start slow = head and travel till slow!=current fast,
        This way we are sure of getting the start node of a cycle, Not by flooks but a verified method

        That's it
    '''
    def detectCycle(self , head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head

        # Check for cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None # No cycle is found , fast has reached end

        # Cycle is found , Find the starting node
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast # or slow , upto you , both are same