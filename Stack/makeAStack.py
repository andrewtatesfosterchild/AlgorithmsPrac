class Stack:

    '''
        What is stack?
        An array in disguise
    '''

    ptr = -1

    def __init__(self , n = 10) -> None:
        self.nums = [None]*n
        print(f"Stack of {n} elements created")
    
    def push(self , item):
        if self.ptr < len(self.nums) - 1:
            self.ptr+=1
            self.nums[self.ptr] = item
            return (f"{item} inserted")
        else:
            return "Stack Overflow"
    def pop(self):
        if self.ptr >= 0:
            remove = self.nums[self.ptr]
            self.nums = self.nums[:-1]
            self.ptr-=1
            return (f"{remove}  removed")
        else:
            return "Stack is empty"
        
    def peek(self):
        try:
            return self.nums[self.ptr]
        except:
            return("Stack is empty")
    
stack = Stack(10)

print(stack.push(5))
print(stack.push(10))
print(stack.push(15))
print(stack.push(20))
print(stack.push(25))
print(stack.push(30))
print(stack.push(35))
print(stack.push(40))
print(stack.push(45))
print(stack.push(50))

print(stack.push(55)) # Overflow call

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.peek()) # 0 elements case

print(stack.pop()) # Stack empty
