class BST:
    class Node:
        def __init__(self , value):
            self.val = value
            self.height = 0
            self.left = None
            self.right = None
        
        def getValue(self):
            return self.val
        
    def __init__(self) -> None:
        self.root = None
    
    def height(node):
        if not node:
            return -1
        
        return node.height
    
    def isEmpty(self):
        return self.root == None
    
    def display(self):
        self._display(self.root, "Root Node: ")
    
    def _display(self , node , details):
        if not node:
            return
        
        print(details + self.getValue(node))

        self._.display(node.left , "Left child of " + str(self.getValue(node)) + " : ")
        self._.display(node.right , "Right child of " + str(self.getValue(node)) + " : ")

    def insert(self , value):
        root = self._insert(value , self.root)

    def _insert(self, value , node):
        if not node:
            node = self.Node(value)
            return node
        if value < node.val:
            node.left = self.insert(value , node.left)
        if value > node.val:
            node.right = self.insert(value , node.right)

        node.height = max(self.height(node.left) + self.height(node.right) + 1)

        return node
    
    def balanced(self):
        return self._balanced(self.root)
    
    def _balanced(self, node):
        if not node:
            return True
        
        return abs(self.height(node.left) - self.height(node.right)) <=1 and self._balanced(node.left) and self._balanced(node.right)
    
    def populate(self , nums):
        for i in range(len(nums)):
            self.insert(nums[i])
    

if __name__ == '__main__':
    bst = BST()
    bst.populate([1,2,3,4,5,6,7,8,9,10])
    bst.display()


