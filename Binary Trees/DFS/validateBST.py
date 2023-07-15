# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Logic: Tweaked DFS Traversal

    '''
        BST has an interesting property
        Left sub-tree nodes' value < current node value
        Right sub-tree nodes' value > current node value

        So, for each value, let's set an upper and lower bound
        which keep changing whilst travelling down the tree

        basic rule is , node.val is greater than lower and smaller than upper bound

        if that's the case, and we go left, since its a BST, no value greater than node.val can further exist. Thus, lower stays as it is and upper changes to root.val

        similarly, if we go towards right, since its a BST, no value smaller than node.val can exist further now, Thus, lower changes to root.val and upper stays as it is

        That's it :coinflip:


    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf') , float(inf))
    
    def helper(self, root , lower, upper):
        if not root:
            return True
        if lower < root.val < upper:
            return (self.helper(root.left , lower , root.val)
            and
            self.helper(root.right , root.val , upper))
        else:
            return False
        
        return True
        
        
        