class BinaryTree:

    def __init__(self) -> None:
        pass

    class Node:
        value = 0
        left = None
        right = None
    
        def Node(self , value):
            self.value = value
    
    root = Node(0)

    def populate(self):
        print("Enter the root node: ")
        value = int(input())
        root = self.Node(value)
        self.populate(root)
    
    def populate(self , node):
        print("Do you want to enter left of ",node.value)
        left = bool(input())
        if left:
            print("Enter the value of the left of ",node.value)
            value = int(input())
            node.left = self.Node(value)
            self.populate(node.left)
        
        print("Do you want to insert to the right of ",node.value)
        right = bool(input())
        if right:
            print("Enter the value of the right of ",node.value)
            value = bool(input())
            node.right = self.Node(value)
            self.populate(node.right)
    
    def display(self):
        self.display(self.root, "")
    
    def display(self , node , indent):
        if not node:
            return
        
        print(indent + node.value)
        self.display(node.left , indent + "\t")
        self.display(node.right , indent + "\t")
    
    def prettyDisplay(self):
        self.prettyDisplay(self.root , 0)
    
    def prettyDisplay(self, node , level):
        if not node:
            return

        self.prettyDisplay(node.right , level + 1)

        if level!=0:
            for i in range(level-1):
                print("|\t\t")
            print("|-------->",node.value)
        else:
            print(node.value)
    
if __name__ == '__main__':
    BinaryTree = BinaryTree()
    BinaryTree.populate()
    BinaryTree.prettyDisplay()