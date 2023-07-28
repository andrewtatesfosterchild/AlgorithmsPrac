class CircularQueue:
    '''
        A snake chasing its own tail , Never to bite , Never to stop , Never to tire , Just chasing forever.
    '''

    def __init__(self , n = 10) -> None:
        self.nums = [None]*n
        self.start = 0
        self.end = 0
        self.len = 0
        print(f"Queue of {n} elements created")
    
    def insert(self , item):
        if not self.isFull():
            self.nums[self.end] = item
            self.end = (self.end + 1) % len(self.nums) # Wrap around and end becomes the first element ,  that is to be removed next
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
            self.start = (self.start + 1) % len(self.nums)
            self.len-=1 # Creating a vacant space
            return f"{remove} removed"
        
    def peek(self):
        if not self.isEmpty():
            return self.nums[self.start]
        else:
            return "Queue is empty"
            
    def display(self):
        if self.isEmpty():
            return "Queue is empty"
        i = self.start
        while True:
            print(self.nums[i] , " -> " , end="")
            i = (i + 1) % len(self.nums)
            if i == self.end:
                break
        print("END")

        
class DynamicCircularQueue(CircularQueue):
    def insert(self , item):
        if self.isFull():
            temp = [None] * (2 * len(self.nums))

            for i in range(len(self.nums)):
                temp[i] = self.nums[(self.start + i) % len(self.nums)] # Simulating moving forward , A left shift
            
            self.start = 0
            self.end = len(self.nums)
            self.nums = temp
        return super().insert(item)

queue = DynamicCircularQueue(5)

queue.insert(5)
queue.insert(5)
queue.insert(5)
queue.insert(5)
queue.insert(5)
queue.display()

queue.insert(6) # Full case exploit check
queue.display()
print(queue.nums) # Extended Queue by twice length of original array
