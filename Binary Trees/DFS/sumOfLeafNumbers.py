# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Logic: Simple DFS Traversal

    '''
    Consider this binary tree
    
                             1
                            / \
                           2   3
                          / \   \
                         4   5   6
                        / \   \
                       7   8   9
        
    The recursion tree will be:

                            sumNumbers(1, 0)
                          /                 \
              helper(2, 10)                 helper(3, 10)
              /        \                     /        \
       helper(4, 120) helper(5, 121)       helper(6, 130)
       /        \           \*                   \
helper(7, 1220) helper(8, 1221)         helper(9, 1310)





    '''
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root , 0)
    
    def helper(self , root , cur):

        if not root:
            return 0

        cur = cur * 10 + root.val # Actually making the number on each call

        if not root.left and not root.right:
            return cur # Returning the number formed on leaf hits
        
        return self.helper(root.left , cur) + self.helper(root.right , cur) # DFS
        
