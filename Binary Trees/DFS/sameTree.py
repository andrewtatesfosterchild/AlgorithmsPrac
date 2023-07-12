# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Logic: DFS Traversal

    '''
        In each recursive call , I'll check if both p and q exist simultaneously, If yes return True else False

        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        Now, We check if both values are equal and recursively keep doing it till one of the above cases are hit
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        where self.isSameTree(p.left,q.left) compares the left subtrees and self.isSameTree(p.right,q.right) compares the right subtrees

        That's it
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # Base case 1
            return True
        elif not p or not q: # Base case 2
            return False
        else:
           return p.val == q.val and self.isSameTree(p.left , q.left) and self.isSameTree(p.right,q.right)