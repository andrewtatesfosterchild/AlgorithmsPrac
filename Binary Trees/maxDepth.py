# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Logic: Good old recursion

    '''
                        Recursiom tree

                          maxDepth(3)
                        /            \
                maxDepth(9)            maxDepth(20)
                    |                   /       \
                    0             maxDepth(15)  maxDepth(7)
                                        |            |
                                        0            0
        This recursion is nothing but instantiating recursion, Go revise it

        For every level, left and right recursion does its job and gets the required base case hit, comes back to the previous level and now both have some value

        Now, we return max(left,right) + 1 which returns the maximum height upto that level

        We take this to the upper level calls of left and right and re-evaluate max(left,right) + 1 for each level till the whole tree is covered

        That's it :coinflip:

    '''

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left = right = 0

        if not root:
            return 0
        
        left = self.maxDepth(root.left) 
        right = self.maxDepth(root.right)

        return max(left,right) + 1 # Returns to the left / right and is re-evaluated for every level