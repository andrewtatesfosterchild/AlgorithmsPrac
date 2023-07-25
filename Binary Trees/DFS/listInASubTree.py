class Solution:
    # Logic: DFS + Basic recursion logic

    '''
        I'll tell you what we did here,

        We need to find the subpaths, So we must check all aspects of the tree, Leaving no stone unturned

        So isSubPath becomes a recursive ally which keeps firing trees to dfs for further evaluation,
        Dfs checks the trees while traversing the LL and if conditions fail it turns false, Then isSubPath fires the left subtree and similarly the right rubtree if left fails too. If everything is False, It returns False

        That's it

        Code with comments for understanding:
        
        if not root: # Sequence needs to exist for subsequences
            return False
        if not head: # Null is a part of every tree
            return True
        
        return self.dfs(head , root) or self.isSubPath(head , root.left) or self.isSubPath(head , root.right)  # Check for head in tree (including node) , If yes then return, If no then check in left and right subtrees

        # Why these different cases wont it be the same thing for left and right subtrees if we check the main tree itself?
        # Good question, What we are searching for is a SubPath which matches the LL, It maybe the in the tree itself which is good, But if its not, Then we have to check the left and the right subtrees to check if it exists, remember we are checking for a subpath inside a tree path
        
    def dfs(self, head , root):
        if not head: # Full Linked list traversed according to return condition, Matching , Return True
            return True
        if not root: # Root exhausted before reaching end of LL
            return False
        
        return head.val == root.val and (self.dfs(head.next , root.left) or self.dfs(head.next , root.right)) # Recursively check if the current head val matches current root val
        # If yes, Just keep traversing as usual
        # If no , Return False and resort to the left or the right subtree wala recursion call, Its our last hope

        That's it to this problem, Nothing else
    '''
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: # Sequence needs to exist for subsequences
            return False
        if not head: # Null is a part of every tree
            return True
        
        return self.dfs(head , root) or self.isSubPath(head , root.left) or self.isSubPath(head , root.right)  # Check for head in tree (including node) , If yes then return, If no then check in left and right subtrees

        # Why these different cases wont it be the same thing for left and right subtrees if we check the main tree itself?
        # Good question, What we are searching for is a SubPath which matches the LL, It maybe the in the tree itself which is good, But if its not, Then we have to check the left and the right subtrees to check if it exists, remember we are checking for a subpath inside a tree path
        
    def dfs(self, head , root):
        if not head: # Full Linked list traversed according to return condition, Matching , Return True
            return True
        if not root: # Root exhausted before reaching end of LL
            return False
        
        return head.val == root.val and (self.dfs(head.next , root.left) or self.dfs(head.next , root.right)) # Recursively check if the current head val matches current root val
        # If yes, Just keep traversing as usual
        # If no , Return False and resort to the left or the right subtree wala recursion call, Its our last hope

        # That's it to this problem, Nothing else