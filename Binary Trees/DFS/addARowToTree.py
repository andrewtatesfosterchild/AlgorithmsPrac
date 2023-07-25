# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Logic: DFS till you reach depth, Then insert on that level

    '''
        This is really an easy problem

        So we are given a depth, Let's use it then!
        Till my depth is not 2, I will keep performing DFS and reducing depth by one

        Now that I know depth is 2,
        Wait stop, WHY DEPTH = 2?*

        Good question, The root node is at depth 1 , According to that we need to insert at depth 2 bacause that means we are inserting on the desired level , AS the og depth is root.depth - depth = 2 - 1 = 1, So you have reached the depth of 1 technically and beyond this must exist your inserted row, That's it , Nothing else here

        So once you reach a depth of 2, Store your previous lefts and rights in a pointer,
        set the root.left as TreeNode(val , prevleft , None)
        and root.right as TreeNode(val , None , prevright)

        Why in root.left, right None and vice versa in right?
        Tell me, Why would you set the previous right subtree in the current left subtree? Think about it xD

        And at last a special case where depth == 1 is given:
        This means insert above the current level as th depth of root is 1
        Thus , We create a newRoot = TreeNode (val , root , None)
        Assigning to right wont work as python calls for the left child of a tree first

        return the newRoot

        That's it, Nothing else



    '''
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1: # If root itself is the node to insert on
            newRoot = TreeNode(val , root , None)
            root = newRoot
            return root


        if not root:
            return

        if depth > 2:
            if root.left:
                self.addOneRow(root.left , val , depth - 1)
  
            if root.right:
                self.addOneRow(root.right , val , depth - 1)
        
        if depth == 2:
        
            prevleft , prevright = root.left , root.right
            root.left = TreeNode(val , prevleft , None)
            root.right = TreeNode(val , None , prevright)

        return root