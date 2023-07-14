# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Logic: Simple & logical node creation

    '''
        It is very clear, We need to construct a binary search tree from the given array

        The array is sorted, What does this mean?
        This means that the middle element will always be the ROOT of the tree (Since well, The array is sorted and BST has a property of left < right and middle is the root)

        Now the root is placed, root.left and root.right will equal the mid of the two subarrays formed by mid partition, Everytime till the base case hits

        That's it, There's nothing else to it

        if len(nums) == 0: 
            return None
        Incase nums is empty

        root = self.helper(nums , 0 , len(nums) - 1)
        Here we set start and end pointers to 0 and len(nums) - 1

        Here's where the fun begins:
        def helper(self , nums, s , e):
            if s > e: 
                return
            Base case , return nothing

            mid = s + (e-s) // 2
            Calculating mid for the current subarray

            root = TreeNode(mid)
            setting mid as the root for the current subtree
            
            root.left = self.helper(nums , s , mid - 1)
            Now the root will be made in the next recursion call for this subarray, That root will be the root.left of the previous root

            root.right = self.helper(nums , mid+1 , e)
            Similarly A root will be made in the next recursion call which will become the root.right for the previous root

            When the recursion is done, 
            return root

        That's it, Done :coinflip: ;)

    '''
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        root = self.helper(nums , 0 , len(nums) -1)
        return root


    def helper(self , nums, s , e):
        if s > e:
            return
        
        mid = s + (e-s) // 2

        root = TreeNode(nums[mid])
        root.left = self.helper(nums , s , mid - 1)
        root.right = self.helper(nums , mid + 1 , e)

        return root

