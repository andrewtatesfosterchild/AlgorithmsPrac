# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    # Logic: Stack or Queue ; Recursion is your ally

    '''
        Ananlyzing this problem was easy , A NestedList object which can contain nestedlists or integers at any point of time

        Why extending the self.nums wont work:
            We tried this , But due to the nested nature of the object, One might end up extending only the outer list and the inner list gets ignored, So , We need a solution which can open every list

            It's more like diving a problem into smaller sub-problems, Reminds you of something? Recursion , that's right.

            Now that we know how we came up with recursion, Let's understand how the recursion works:
            addInteger is my recursive function,
            I run a for loop for every nested object in the nestedlist, Mind that till now I have no idea that it is an integer or a list.
            Then , We will use the isInteger() method to determine if it is an integer, It it is , We can simply append it
            Else? Else what, This is a list, And this might contain other nested lists
            Simply call the addInteger with a getList() on the element and in the next recursion call, If an integer is encounter it will be appended and if a nested list is encountered again , Recursion will handle the rest

            That's it , Question done
    '''
    def __init__(self, nestedList: [NestedInteger]):

        self.q = deque([]) # Initializing a deque
        self.addInteger(nestedList) # Recursive function to open and append all lists

    def next(self) -> int:
        if self.hasNext():
            return self.q.popleft()
        
    
    def hasNext(self) -> bool:
        return bool(self.q)
    
    def addInteger(self , nestedList):
        for element in nestedList:
            if element.isInteger():
                self.q.append(element.getInteger())
            else:
                self.addInteger(element.getList()) # Recursively calling till all the lists are opened & converted to integers
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())