class MyQueue:

    # Logic: Two stacks make a queue

    '''
        Stack is LIFO, Queue is FIFO
        Take all the pushes in the main stack

        On every pop,
        Append every element popped from stack 1 into stack 2 , That way last element is on top
        Pop the element from stack 2
        store it in a variable , then again empty stack2 and store in stack1
        return remove

        for peek just show the stack's top

        isEmpty returns True when the stack has 0 length

        That's it


    '''

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        remove = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
            
        return remove
        

    def peek(self) -> int:
        if not self.empty():
            return self.stack1[0]
        else:
            return False        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()