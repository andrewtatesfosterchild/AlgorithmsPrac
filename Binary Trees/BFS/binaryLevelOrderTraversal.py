# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Logic: BFS Implementation using Queue

    '''
        BFS Takes some time to digest, So be it.

        In this question, Level order nodes are asked, We will use a Deque to store the root of the binary an empty var ans = []

        while len(queue): Running for all the levels Tree

            qlen , row = len(queue) , []
            qlen is the length of the current level, row is empty initially

            for _ in range(qlen):
                curr = queue.popleft()
                removes the left val from queue and stores in curr
                row.append(curr.val)
                appends value of curr node to row

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                Checks if left and right childs exists and if they do appends it to the queue

            ans.append(row)
            A row is processed, we store it in ans
        
        return ans

        That's it


    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue , ans = deque([root] if root else []) , []
        
        while len(queue):
            qlen , row = len(queue) , []
            
            for _ in range(qlen):
                curr = queue.popleft()
                row.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            ans.append(row)
        
        return ans
        

