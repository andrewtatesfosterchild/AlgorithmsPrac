# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Logic: Plain old DFS ; Also you need to start drawing recursion trees

    '''
        There was nothing to this problem, Its a BST that was given, Any order that was given.

        What had to be done? Insert a node into bst, On what basis can we do this?
        That's right , By comparing values of the current root and given node

        By setting return to TreeNode(val), I achieve two things:
        1. Obviously the infamous no root given case
        2. When I'm traversing in a DFS and hit a leaf node and go beyond it, That's where I need to assign my node

        For the second purpose, We keep making root.left = self.helper(root.left , val) and root.right = self.helper(root.right , val)

        So when it goes beyond a leaf, It returns a Treenode val which attaches itself to the particular branch the recursion was calle up, and returns keep returning and at last, We return the root

        That WAS IT, Draw recursion trees dude fr
    '''
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.helper(root , val)


    def helper(self , root , val):
        if not root:
            return TreeNode(val)
        
        if  val < root.val:
            root.left = self.helper(root.left , val)
        else:
            root.right = self.helper(root.right , val)
        
        return root


