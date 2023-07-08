# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # Logic: This is the most easiest, Most unfathomable , Most hilarious , Most painful yet the most badass problem of linkedlist I have ever seen

        '''
            All the values of the linked list are unique, and "It is guaranteed that the given node node is not the last node in the linked list".

            For the sake of heavens I'll repeat this again:
            "It is guaranteed that the given node node is not the last node in the linked list"

            If you missed this hint, You won't be able to solve this problem

            A node is given , Not the head but a node

            Go ahead, Delete this node, The problem says

            No head, No traversal , HOW?!

            The answer lies in the hint

            The node provided will never be the tail node, This hints us to use the nextnode we would like

            Thus, I'll take my opportunity and set 
            nextnode = node.next

            Now, I'll update the current node's value with the next node's value
            node.val = nextnode.val

            Finally, I'll set the node to point to the nextnode's next node, Meaning the node has been erased without disturbing its own links

            node.next = nextnode.next

            Now take a careful look at another hint:
                "All the values of the linked list are unique"
            
            But why? Imagine them not being unique, How would we know which node has been deleted without a traversal, That is why the nodes are UNIQUE


            That's it, Done

            I love this question man

        '''
        
        nextnode = node.next
        node.val = nextnode.val
        node.next = nextnode.next

            

