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
        if self.isFull():
            self.ptr+=1
            self.nums[self.ptr] = item
            return (f"{item} inserted")
        
    def pop(self):
        if self.isEmpty():
            remove = self.nums[self.ptr]
            self.nums[self.ptr] = None
            self.ptr-=1
            return (f"{remove}  removed")
        else:
            return "Stack is empty"
        
    def isFull(self):
        if self.ptr < len(self.nums) - 1:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.ptr >= 0:
            return True
        else:
            return False
        
    def peek(self):
        if self.isEmpty():
            return self.nums[self.ptr]
        else:
            return "Stack is empty"

class DynamicStack(Stack):
    def __init__(self, n=10) -> None:
        super().__init__(n)

    def push(self , item):
        if not super().isFull():
            self.temp = [None] * (2 * len(self.nums))
            self.nums.extend(self.temp)
        return super().push(item)
        
# stack = Stack(10)

# print(stack.push(5))
# print(stack.push(10))
# print(stack.push(15))
# print(stack.push(20))
# print(stack.push(25))
# print(stack.push(30))
# print(stack.push(35))
# print(stack.push(40))
# print(stack.push(45))
# print(stack.push(50))

# print(stack.push(55)) # Overflow call

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print(stack.peek()) # 0 elements case

# print(stack.pop()) # Stack empty

dstack = DynamicStack(5)

print(dstack.push(1))
print(dstack.push(2))
print(dstack.push(3))
print(dstack.push(4))
print(dstack.push(5))

print(dstack.push(6)) # Checking the overridden method
print(dstack.peek()) # Verifying

print(dstack.pop())
print(dstack.pop())
print(dstack.pop())
print(dstack.pop())
print(dstack.pop())
print(dstack.pop())

print(dstack.pop()) # Checking stack empty

print(dstack.peek()) # Verifying

print(dstack.nums) # Finally
