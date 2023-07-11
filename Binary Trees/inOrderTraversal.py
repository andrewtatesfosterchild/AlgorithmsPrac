# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ast import List
from typing import Optional


class Solution:

    # Logic: Primitive Inorder traversal recursion logic

    '''
        This is the utmost basic you can get out of anything

        Remember this
    '''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper (root , res)
        return res

    def helper(self, root , res):
        if root:
            self.helper(root.left , res)
            res.append(root.val)
            self.helper(root.right , res)