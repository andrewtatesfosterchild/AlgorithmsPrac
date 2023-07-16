# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Logic: I: Tweaked Preorder traversal + II: Node assignment

    '''
        This was the first medium I solved without any help :)
        I'm fucking proud of myself , Keep the thing up

        Okay, Let's get to the chase
        The question says the linked list follows a preorder traversal
        So? Do it and store the result in a list

        The question asks for one more thing from you, The root.left should be null for all nodes, How would you do that?
        Just add a single line to the preorder traversal
        'root.left = None'

        something like this:

        preorder.append(root.val)
        self.helper(root.left , preorder)
        self.helper(root.right , preorder)
        root.left = None

        Now heres the fun, Everytime a tree wall hits, The value of this node is appended, Now It goes back to the previous node, takes its value and sets the root.left to null

        The entire tree's root.left is null now

        Now that you have the preorder list,
        All that remains is making new nodes and assigning them the values of preorder

        Iterate through and keep assigning

        for i in range(len(preorder)):
            rootholder.val = preorder[i]
            if rootholder.right:
                rootholder = rootholder.right
            else:
                if i < len(preorder) - 1:
                    rootholder.right = TreeNode()
                    rootholder = rootholder.right
            
            All things above is basic stuff, But why i < len(preorder) - 1?
            Because if we are at the last node we need not create another empty node

            That's it, Well done

        
    '''
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root: # If no root present
            return

        preorder = [] # Initializing empty preorder list

        preorder= self.helper(root, preorder) # Calling helper funtion for preorder

        rootholder = root # Separate pointer for traversing as root is being returned, If root is changed output will be affected

        for i in range(len(preorder)): # Loop till all the nodes fulfilled
            rootholder.val = preorder[i] # Sets the value for the current node to preorder val
            if rootholder.right: # If a node already exists in right, No need to create a new one, Just shift to the node in right
                rootholder = rootholder.right
            else: # Node doesn't exist, We need to make a new one
                if i < len(preorder) - 1: # Preventing the loop to create one extra node at the last
                    rootholder.right = TreeNode()
                    rootholder = rootholder.right




    def helper(self, root , preorder):
        
        if not root:
            return

        preorder.append(root.val)
        self.helper(root.left , preorder)
        self.helper(root.right , preorder)
        root.left = None # The only tweak required, Sets all the lefts on the binary tree nodes to null

        return preorder