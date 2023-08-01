# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Logic: DFS ; Locate the max index , Left immediately becomes elements till max index and right becomes elements from max index till end

    '''
        Exactly same as what we thought
        if not nums:
            simply return None
        
        Each time you enter the recursion call , Calculate the max element and its index
        The max element will become your root ALWAYS

        Now the question is , How do you determine the left subtree and the right subtree.
        The logic behind this is that I want to move towards max index for left and from max index towards end, This intuition should be clear

        Now if I do this , How will it affect my tree in the next recursion?
        In the next recursion left subarray is passed to the root.left and right subarray of this call is passed to the next call

        What after this sherlock? -_-

        After this? The code again selects a max element and its index, Again it passes the left subtree till the new max and right subtree from the new max

        At some time while doing this, The subarrays will be empty, Which means we have reached the leaf node, Which means we will start going up now?

        Now focus again on our recursion, At every level, The root was already set as the max element of that array AT FIRST

        While returning, The DFS used will set the left links and right correctly

        After the left part is done, Recursion comes back to the main root, And starts setting root.right, Again for root.right every level's max element is set as the root element of that subtree, And the left and the right subtrees are decided as the left subarrays and the right subarrays towards the mex element and from the max element of that recursion call

        That's it, What was so tough about it?
        Cool? Easy, Done
    '''
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        max_value = max(nums)
        max_index = nums.index(max_value)

        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])

        return root
