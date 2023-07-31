class MyCircularDeque:

    # Logic: This is actually a good problem

    '''
        This is the next version of dynamic circular queue
        The dynamic circular deque

        What are supposed to do? How does the circle work?
        Traditionally like with some great queue implementations , This too requires a two pointer approach, Both the pointers are initially on head

        You know how a deque works, The task is to just make it circular

        So the functions like Insertleft , InsertRight , DeleteLeft , DeleteRight are going to stay the same , But with a slight twist of circular

        How do you insertleft?
        That's a terrible question watson tf do you mean how do you insertleft -_-
        Well, That's it then, Do the same, Insert on the LEFT GODAMMIT?!

        But wait! There are some conditions here
        If the queue is empty, Go ahead insert at left

        If the queue is full,
        You can't insert , Don't try please

        else: It is the CIRCULAR CASE
        We are going to insert at left, No matter what happens
        After inserting , decrease left , Now if left goes beyond 0 as in -1  , % k
        That's it, We go to the second last index of the array

        then? increment qlen and just return True

        Similarly for inserRight,
        isFull? Return False, isEmpty? insert at Right

        else: The circular case:
            when inserted at right , right + =1 and if it goes beeyond arraylength % k brings it back to the first position of the array
            increase the qlen
        
        For deleteleft,
        Dont delete from an emptylist -_-
        else:
            delete from left , in python turn it to None or something else
            left increases after this, But if it goes beyond k , Pull it back to zero
            decrease array size
            if it becomes empty,
            queue is at initial state , set both pointers at 0 again
        
        For deleteright,
        Dont delete from an emptylist
        else: The usual
            delete from right , right goes -1 till it goes beyond k and gets pulled back to second last position
            if queue is empty after this, both pointers 0
        
        For getleft getright,
        Just return values at left and right

        For isFull isEmpty,
        just return if qlen == len of arr

        That's it, Done

    '''

    def __init__(self, k: int):
        self.q = [-1]*k
        self.l = 0
        self.r = 0
        self.qlen = 0
        self.k = k

        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.q[self.l] = value
        else:
            self.l = (self.l - 1) % self.k
            self.q[self.l] = value
        self.qlen+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.q[self.r] = value
        else:
            self.r = (self.r + 1) % self.k
            self.q[self.r] = value
        self.qlen+=1
        return True

        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.l] = -1
        self.l = (self.l + 1) % self.k
        self.qlen-=1
        if self.isEmpty():
            self.r = self.l
        return True

        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.r] = -1
        self.r = (self.r - 1) % self.k
        self.qlen-=1
        if self.isEmpty():
            self.l = self.r
        return True
        

    def getFront(self) -> int:
        return self.q[self.l]
        

    def getRear(self) -> int:
        return self.q[self.r]
        

    def isEmpty(self) -> bool:
        return self.qlen == 0
        

    def isFull(self) -> bool:
        return self.qlen == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()