class CircularQueue:
    '''
        A snake chasing its own tail , Never to bite , Never to stop , Never to tire , Just chasing forever.
    '''
    start = 0
    end = 0
    len = 0

    def __init__(self , n = 10) -> None:
        self.nums = [None]*n
        print(f"Queue of {n} elements created")
    
    def insert(self , item):
        if not self.isFull():
            self.nums[self.end] = item
            self.end+=1
            self.end = self.end % len(self.nums) # Wrap around and end becomes the first element ,  that is to be removed next
            self.len+=1
            return (f"{item} inserted")
        else:
            return "Queue is Full"
    
    def isFull(self):
        return self.len == len(self.nums)

    def isEmpty(self):
        return self.len == 0
    
    def remove(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            remove = self.nums[self.start]
            self.nums[self.start] = None
            self.start+=1
            self.start = self.start % len(self.nums)
            self.len-=1 # Creating a vacant space
            return f"{remove} removed"
    def peek(self):
        if not self.isEmpty():
            return self.nums[self.start]
        else:
            return "Queue is empty"
            
    def display(self):
        i = self.start
        while i != self.end:
            print(self.nums[i] , " <- " , end="")
            i+=1
            if i == self.end:
                break
            else:
                i = i % len(self.nums)
        print("END")

        
queue = CircularQueue(5)
print(queue.insert(5))
print(queue.peek()) # Verifying
print(queue.insert(4))
print(queue.peek()) # Verifying
print(queue.insert(3))
print(queue.peek()) # Verifying
print(queue.insert(2))
print(queue.peek()) # Verifying
print(queue.insert(1))
print(queue.peek()) # Verifying



print(queue.nums)
print(queue.peek())

print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove()) # Last Removed

print(queue.insert(5))
print(queue.insert(5))
print(queue.insert(5))
print(queue.insert(11))
print(queue.peek())

queue.display()