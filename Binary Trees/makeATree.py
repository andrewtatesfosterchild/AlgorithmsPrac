class BinaryTree:
    class Node:
        def __init__(self , value): # Corrected node initialization
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self): # Corrected Tree initialization
        self.root = None
    

    def populate(self , node):
        print(f"Do you want to enter the left child of {node.value}? (y/n)") # Condition check made easier for user
        left = input().lower() == 'y'
        if left:
            print(f"Enter the value of the left child of {node.value}:")
            value = int(input())
            node.left = self.Node(value)
            self.populate(node.left)

        print(f"Do you want to enter the right child of {node.value}? (y/n)") # Same, Condition fixed
        right = input().lower() == 'y'
        if right:
            print(f"Enter the value of the right child of {node.value}:")
            value = int(input())
            node.right = self.Node(value)
            self.populate(node.right)
    
    ######## Removed Helper Function to populate ########
    
    def display(self):
        self._display(self.root, "")
    
    def _display(self , node , indent): # Fixed Polymorphism
        if not node:
            return
        
        print(indent + str(node.value))
        self._display(node.left , indent + "\t")
        self._display(node.right , indent + "\t")
    
    def prettyDisplay(self):
        self._prettyDisplay(self.root, 0)
    
    def _prettyDisplay(self, node, level):
        if not node:
            return

        self._prettyDisplay(node.right, level + 1)

        if level != 0:
            print("\t" * (level-1) + "|-------->", node.value)
        else:
            print(node.value)
    
if __name__ == '__main__':
    binaryTree = BinaryTree()
    print("Enter the root node:") # It asks for root here now
    value = int(input())
    binaryTree.root = binaryTree.Node(value) # Setting root with object
    binaryTree.populate(binaryTree.root) # Calling populate for insertions
    binaryTree.prettyDisplay() # Displaying the tree