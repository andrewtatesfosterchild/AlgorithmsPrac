class Queue:
    '''
        What is Queue?
        A linked list in disguise
    '''

    end = 0

    def __init__(self , n = 10) -> None:
        self.nums = [None]*n
        print(f"Queue of {n} elements created")
    
    def insert(self , item):
        if not self.isFull():
            self.nums[self.end] = item
            self.end+=1
            return (f"{item} inserted")
        else:
            return "Queue is Full"
    
    def isFull(self):
        return self.end == len(self.nums)

    def isEmpty(self):
        return self.end == 0
    
    def remove(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            remove = self.nums[0]
            self.nums = self.nums[1:] + [None] # Simulating a left shift, This takes O(N) time and can be solved using circular queue
            self.end-=1 # A vancant space created
            return f"{remove} removed"
    def peek(self):
        if not self.isEmpty():
            return self.nums[0]
        else:
            return "Queue is empty"
            
queue = Queue(5)
print(queue.insert(5))
print(queue.insert(4))
print(queue.insert(3))
print(queue.insert(2))
print(queue.insert(1))

print(queue.insert(0)) # Overflow case
print(queue.nums)
print(queue.peek()) # Verifying

print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())

print(queue.remove()) # Underflow case

print(queue.nums)
print(queue.peek())

print(queue.insert(5))
print(queue.nums) # Final check