# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #Logic: Simple traversal & Checks

    '''
        This qtn is very similar to Same trees
        Here, We send the left and right subtrees to helper function and check for all cases
        if not p and not q:
            return True
        Both subtrees are missing? Symmetry obtained
        elif not p or not q:
            return False
        One of them missing? Symmetry lost
        else:
            return p.val == q.val and self.isMirror(p.left , q.right) and self.isMirror(p.right , q.left)
            checking the val if both are present, And recursively calling left of p and right of q, and right of p and left of q, to check symmetry. First it checks p.left and q.right (since its a mirror check and that's how mirrors behave you walnut brain -_-) and similarly it checks for p.right and q.left(Don't ask me the reason again -_-)

            That's it, :coinflip:

            Below is an example, Which clearly states my point

            Suppose we have the following binary tree:

                             1
                            / \
                           2   2
                          / \ / \
                         3  4 4  3

            We want to determine if this tree is symmetric.

            We start by calling the isSymmetric function with the root of the tree, which is the node with value 1.

            Inside the isSymmetric function, it calls the isMirror function with the left and right subtrees of the root.

                Left subtree:
                     2
                    / \
                   3   4

                Right subtree:

                     2
                    / \
                   4   3

            Now, let's look at how the isMirror function works for this example:

            p is the left subtree with the root node 2, and q is the right subtree with the root node 2.

            Since both p and q are not None, we proceed to the next condition.

            We check if the values of p and q are equal. In this case, they are both 2, so the condition is satisfied.

            Now, we recursively call isMirror for the following cases:

            p.left (node 3) and q.right (node 3).
            p.right (node 4) and q.left (node 4).
            The recursion continues to the next level.

            At the next level, the isMirror function is called with nodes 3 and 3. Both p and q are not None, and their values are equal (both 3).

            Again, we recursively call isMirror for the following cases:

            p.left is None, and q.right is None.
            p.right is None, and q.left is None.
            Since both p.left and q.right are None, and both p.right and q.left are None, the recursion reaches the base case where both subtrees are missing. Therefore, the function returns True at this level.

            Going back to the previous level, we still need to check the second case, which is p.right (node 4) and q.left (node 4).

            Both p.right and q.left are not None, and their values are equal (both 4).

            We recursively call isMirror for the following cases:

            p.left is None, and q.right is None.
            p.right is None, and q.left is None.
            Similar to the previous case, the recursion reaches the base case where both subtrees are missing, and the function returns True.

            Finally, back to the isSymmetric function, it receives True from both calls to isMirror for the left and right subtrees. Since both subtrees are symmetric, the isSymmetric function also returns True.


    '''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left , root.right)
        
    def isMirror(self, p , q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isMirror(p.left , q.right) and self.isMirror(p.right , q.left)